"""Unit tests for gpuai_sdk.jobs against a small in-process fake of /v1/jobs.

The fake keeps jobs in memory and moves a job through queued -> running ->
succeeded as it is polled, appending a log chunk on each step, which is
roughly what the scheduler and the machine's agent do. The real service is
covered by the Go handler tests and by a live run against demo.
"""

import io
import json
import os
import threading
import zipfile
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

import pytest

import gpuai_sdk
import gpuai_sdk.exceptions
from gpuai_sdk.jobs import JobFailed, JobOutputsUnavailable, JobsClient, JobTimeout


def _zip(files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, data in files.items():
            zf.writestr(name, data)
    return buf.getvalue()


def _now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _job(job_id, body, status="queued"):
    return {
        "id": job_id,
        "name": body.get("name", ""),
        "image": body.get("image", ""),
        "command": body.get("command") or [],
        "env_names": sorted((body.get("env") or {}).keys()),
        "secrets": body.get("secrets") or [],
        "gpu_type": body.get("gpu_type", ""),
        "min_vram_gb": body.get("min_vram_gb", 0),
        "memory_hint_mb": None,
        "compute_hint_pct": None,
        "timeout_seconds": body.get("timeout_seconds", 3600),
        "max_wait_seconds": 0,
        "allow_sharing": False,
        "allow_restart": False,
        "isolation": "soft",
        "mig_profile": None,
        "checkpoint_path": None,
        "max_retries": 2,
        "max_price_per_hour": body.get("max_price_per_hour"),
        "trial_funded": False,
        "status": status,
        "status_reason": None,
        "cancel_requested": False,
        "attempt": 0,
        "retries": 0,
        "evictions": 0,
        "oom_exits": 0,
        "reservation_mb": None,
        "whole_gpu": None,
        "predicted_mb": None,
        "prediction_source": None,
        "predicted_compute_pct": None,
        "compute_prediction_source": None,
        "peak_memory_mb": None,
        "gpu_memory_total_mb": None,
        "util_mean_pct": None,
        "busy_pct": None,
        "memory_source": None,
        "sharing_mode": None,
        "gpu_seconds": 0,
        "attributed_cost_usd": 0,
        "exit_code": None,
        "created_at": _now(),
        "started_at": None,
        "finished_at": None,
    }


class FakeAPI:
    def __init__(self):
        self.jobs = {}
        self.logs = {}  # job id -> list of chunk dicts
        self.bodies = []  # POST /jobs bodies
        self.keys = []  # Idempotency-Key per POST /jobs
        self.auth = []  # Authorization headers seen
        self.fail_next = []  # (status, code) to return before serving
        self.final_status = "succeeded"
        self.steps = 3  # GETs of a job before it finishes
        self.hold = False  # never finish
        self.next_id = 0
        self.outputs = {}  # job id -> zip bytes
        self.blob_auth = []  # Authorization headers seen on /blob
        self.blob_fail = []  # statuses to return from /blob before serving
        self.uploads = {}  # input id -> bytes PUT
        self.lock = threading.Lock()
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), self._handler())
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    @property
    def base(self):
        return f"http://127.0.0.1:{self.server.server_address[1]}/v1"

    def add_log(self, job_id, text):
        chunks = self.logs.setdefault(job_id, [])
        chunk_id = sum(len(c) for c in self.logs.values()) + 1
        chunks.append({"id": chunk_id, "attempt": 1, "text": text, "created_at": _now()})

    def advance(self, job):
        """One poll of a job: move it one step on and log the step."""
        if job["status"] in ("succeeded", "failed", "cancelled") or self.hold:
            return
        job["_polls"] = job.get("_polls", 0) + 1
        if job["_polls"] == 1:
            job["status"] = "running"
            job["started_at"] = _now()
            self.add_log(job["id"], "starting\n")
        elif job["_polls"] >= self.steps:
            job["status"] = self.final_status
            job["finished_at"] = _now()
            job["exit_code"] = 0 if self.final_status == "succeeded" else 3
            if self.final_status == "failed":
                job["status_reason"] = "the command exited with code 3"
            # The last chunk lands just after the status flips, as it can live.
            self.add_log(job["id"], "done\n")
        else:
            self.add_log(job["id"], f"step {job['_polls']}\n")

    def _handler(self):
        api = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _send(self, status, body=None):
                data = b"" if body is None else json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def _problem(self, status, code, detail="nope"):
                self._send(status, {"type": "about:blank", "title": code, "status": status, "detail": detail, "code": code})

            def _public(self, job):
                return {k: v for k, v in job.items() if not k.startswith("_")}

            def _blob(self, method, url):
                """The object store: presigned links, no API key."""
                api.blob_auth.append(self.headers.get("Authorization"))
                name = url.path.split("/")[-1]
                if method == "PUT":
                    n = int(self.headers.get("Content-Length") or 0)
                    api.uploads[name] = self.rfile.read(n)
                    self.send_response(200)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                if api.blob_fail:
                    status = api.blob_fail.pop(0)
                    self.send_response(status)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                data = api.outputs[name]
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def _route(self, method):
                if self.path.startswith("/blob/"):
                    return self._blob(method, urlsplit(self.path))
                api.auth.append(self.headers.get("Authorization"))
                with api.lock:
                    if api.fail_next:
                        status, code = api.fail_next.pop(0)
                        return self._problem(status, code)
                    url = urlsplit(self.path)
                    q = parse_qs(url.query)
                    parts = url.path.split("/")[2:]  # after /v1
                    if parts[0] != "jobs":
                        return self._problem(404, "not_found")
                    if method == "POST" and parts == ["jobs"]:
                        n = int(self.headers.get("Content-Length") or 0)
                        body = json.loads(self.rfile.read(n) or b"{}")
                        api.bodies.append(body)
                        api.keys.append(self.headers.get("Idempotency-Key"))
                        api.next_id += 1
                        job = _job(f"job_{api.next_id}", body)
                        api.jobs[job["id"]] = job
                        return self._send(201, self._public(job))
                    if method == "GET" and parts == ["jobs"]:
                        items = sorted(api.jobs.values(), key=lambda j: j["id"], reverse=True)
                        if "status" in q:
                            items = [j for j in items if j["status"] == q["status"][0]]
                        start = int(q.get("cursor", ["0"])[0])
                        limit = int(q.get("limit", ["100"])[0])
                        page = items[start : start + limit]
                        nxt = str(start + limit) if start + limit < len(items) else None
                        return self._send(200, {"data": [self._public(j) for j in page], "next_cursor": nxt})
                    if parts == ["jobs", "gpu-types"]:
                        return self._send(
                            200,
                            {
                                "complete": True,
                                "data": [
                                    {
                                        "gpu_type": "a100_80gb",
                                        "vram_gb": 80,
                                        "available_now": True,
                                        "price_per_gpu_hour": 1.29,
                                        "last_seen_at": _now(),
                                    }
                                ],
                            },
                        )
                    if parts == ["jobs", "trial"]:
                        return self._send(
                            200,
                            {"enabled": True, "eligible": True, "cap_cents": 2500, "credited_cents": 0, "remaining_cents": 2500, "message": "Your first jobs are free, up to $25."},
                        )
                    if method == "POST" and parts == ["jobs", "inputs"]:
                        n = int(self.headers.get("Content-Length") or 0)
                        body = json.loads(self.rfile.read(n) or b"{}")
                        api.bodies.append(body)
                        later = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat().replace("+00:00", "Z")
                        return self._send(
                            201,
                            {
                                "id": "jfile_in1",
                                "filename": body["filename"],
                                "bytes": body["bytes"],
                                "upload_url": f"http://127.0.0.1:{api.server.server_address[1]}/blob/jfile_in1",
                                "upload_expires_at": later,
                                "expires_at": later,
                                "max_bytes": 1 << 30,
                            },
                        )
                    job = api.jobs.get(parts[1])
                    if job is None:
                        return self._problem(404, "not_found", "job not found")
                    if method == "GET" and len(parts) == 2:
                        api.advance(job)
                        return self._send(200, self._public(job))
                    if method == "POST" and parts[2:] == ["cancel"]:
                        if job["status"] not in ("succeeded", "failed", "cancelled"):
                            job["status"] = "cancelled"
                            job["finished_at"] = _now()
                        return self._send(200, self._public(job))
                    if method == "GET" and parts[2:] == ["outputs"]:
                        base = {"outputs_path": "/outputs", "files": [], "max_bytes": 2 << 30}
                        if job["status"] not in ("succeeded", "failed", "cancelled"):
                            return self._send(200, {**base, "status": "pending", "message": "Files the job writes to /outputs are uploaded when it ends."})
                        data = api.outputs.get(job["id"])
                        if data is None:
                            return self._send(200, {**base, "status": "none", "message": "The job wrote no files to /outputs."})
                        later = (datetime.now(timezone.utc) + timedelta(minutes=15)).isoformat().replace("+00:00", "Z")
                        return self._send(
                            200,
                            {
                                **base,
                                "status": "available",
                                "message": "Kept until later.",
                                "filename": f"{job['id']}-outputs.zip",
                                "bytes": len(data),
                                "files": [{"path": "result.txt", "bytes": 2}],
                                "attempt": 1,
                                "created_at": _now(),
                                "expires_at": later,
                                "url": f"http://127.0.0.1:{api.server.server_address[1]}/blob/{job['id']}",
                                "url_expires_at": later,
                            },
                        )
                    if method == "GET" and parts[2:] == ["logs"]:
                        after = int(q.get("after", ["0"])[0])
                        limit = int(q.get("limit", ["100"])[0])
                        chunks = [c for c in api.logs.get(job["id"], []) if c["id"] > after][:limit]
                        nxt = max([after] + [c["id"] for c in chunks])
                        return self._send(200, {"data": chunks, "next_after": nxt})
                    return self._problem(404, "not_found")

            def do_GET(self):
                self._route("GET")

            def do_POST(self):
                self._route("POST")

            def do_PUT(self):
                self._route("PUT")

        return Handler


@pytest.fixture
def api(monkeypatch):
    fake = FakeAPI()
    monkeypatch.setenv("GPUAI_API_KEY", "gpuai_test_key")
    monkeypatch.setenv("GPUAI_API_BASE", fake.base)
    # Keep the tests fast: no settle wait and no backoff sleeps.
    monkeypatch.setattr("gpuai_sdk.jobs._client._LOG_SETTLE_SECONDS", 0.0)
    monkeypatch.setattr("gpuai_sdk.jobs._client.time.sleep", lambda s: None)
    yield fake
    fake.server.shutdown()


def test_client_reads_key_and_base_from_env(api):
    jobs = JobsClient()
    jobs.gpu_types()
    assert api.auth[-1] == "Bearer gpuai_test_key"


def test_missing_key_is_a_clear_error(monkeypatch):
    monkeypatch.delenv("GPUAI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="GPUAI_API_KEY"):
        JobsClient()


def test_submit_builds_the_body_and_sends_an_idempotency_key(api):
    jobs = JobsClient()
    job = jobs.submit(
        "python eval.py --shard 3",
        gpu_type="a100_80gb",
        image="ghcr.io/acme/eval:1",
        env={"SHARD": "3"},
        repo={"url": "https://github.com/acme/evals", "ref": "main"},
        timeout_seconds=600,
        max_price_per_hour=2.5,
    )
    assert isinstance(job, gpuai_sdk.Job)
    assert job.status == "queued"
    body = api.bodies[-1]
    assert body["command"] == ["python", "eval.py", "--shard", "3"]
    assert body["gpu_type"] == "a100_80gb"
    assert body["env"] == {"SHARD": "3"}
    assert body["repo"] == {"url": "https://github.com/acme/evals", "ref": "main"}
    assert body["timeout_seconds"] == 600
    assert body["max_price_per_hour"] == 2.5
    assert "script" not in body and "name" not in body
    assert api.keys[-1]


def test_submit_rejects_an_unknown_field_before_sending(api):
    jobs = JobsClient()
    with pytest.raises(Exception):
        jobs.submit(["true"], gpu_type="a100_80gb", timeout_seconds="soon")
    assert api.bodies == []


def test_submit_retries_a_5xx_with_the_same_key(api):
    api.fail_next = [(503, "unavailable"), (409, "idempotency_conflict")]
    jobs = JobsClient()
    job = jobs.submit(["true"], gpu_type="a100_80gb", idempotency_key="work-item-7")
    assert job.id == "job_1"
    assert api.keys == ["work-item-7"]  # the two refusals never reached the store
    assert len(api.bodies) == 1


def test_submit_does_not_retry_a_422(api):
    api.fail_next = [(422, "validation_failed")]
    jobs = JobsClient()
    with pytest.raises(gpuai_sdk.ApiException) as exc:
        jobs.submit(["true"], gpu_type="nope")
    assert exc.value.status == 422
    assert api.fail_next == []
    assert api.bodies == []


def test_wait_returns_the_finished_job(api):
    jobs = JobsClient()
    job = jobs.submit(["true"], gpu_type="a100_80gb")
    done = jobs.wait(job.id)
    assert done.status == "succeeded"
    assert done.exit_code == 0


def test_wait_raises_job_failed_when_asked(api):
    api.final_status = "failed"
    jobs = JobsClient()
    job = jobs.submit(["false"], gpu_type="a100_80gb")
    assert jobs.wait(job.id).status == "failed"
    job = jobs.submit(["false"], gpu_type="a100_80gb")
    with pytest.raises(JobFailed) as exc:
        jobs.wait(job.id, raise_on_failure=True)
    assert exc.value.job.exit_code == 3
    assert "exited with code 3" in str(exc.value)


def test_wait_times_out_and_leaves_the_job_running(api, monkeypatch):
    api.hold = True
    clock = iter(range(0, 1000, 10))
    monkeypatch.setattr("gpuai_sdk.jobs._client.time.monotonic", lambda: next(clock))
    jobs = JobsClient()
    job = jobs.submit(["sleep", "999"], gpu_type="a100_80gb")
    with pytest.raises(JobTimeout) as exc:
        jobs.wait(job.id, timeout=25)
    assert exc.value.job.status == "queued"
    assert api.jobs[job.id]["status"] == "queued"


def test_stream_logs_yields_everything_including_the_trailing_chunk(api):
    jobs = JobsClient()
    job = jobs.submit(["python", "eval.py"], gpu_type="a100_80gb")
    assert "".join(jobs.stream_logs(job.id)) == "starting\nstep 2\ndone\n"
    assert jobs.logs(job.id) == "starting\nstep 2\ndone\n"


def test_stream_logs_of_a_job_finished_long_ago_returns_at_once(api, monkeypatch):
    monkeypatch.setattr("gpuai_sdk.jobs._client._LOG_SETTLE_SECONDS", 3600.0)
    jobs = JobsClient()
    job = jobs.submit(["true"], gpu_type="a100_80gb")
    stored = api.jobs[job.id]
    stored["status"] = "succeeded"
    stored["finished_at"] = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
    api.add_log(job.id, "old output\n")
    assert list(jobs.stream_logs(job.id)) == ["old output\n"]


def test_logs_pages_through_more_than_one_response(api):
    jobs = JobsClient()
    job = jobs.submit(["true"], gpu_type="a100_80gb")
    for i in range(1200):
        api.add_log(job.id, f"{i}\n")
    text = jobs.logs(job.id)
    assert text.splitlines() == [str(i) for i in range(1200)]


def test_run_streams_output_and_returns_the_job(api):
    jobs = JobsClient()
    seen = []
    done = jobs.run(["python", "eval.py"], gpu_type="a100_80gb", on_output=seen.append)
    assert done.status == "succeeded"
    assert "".join(seen) == "starting\nstep 2\ndone\n"


def test_run_prints_by_default(api, capsys):
    JobsClient().run(["true"], gpu_type="a100_80gb")
    assert capsys.readouterr().out == "starting\nstep 2\ndone\n"


def test_run_raises_on_failure(api):
    api.final_status = "failed"
    with pytest.raises(JobFailed):
        JobsClient().run(["false"], gpu_type="a100_80gb", on_output=None)


def test_run_cancels_the_job_on_timeout(api, monkeypatch):
    api.hold = True
    clock = iter(range(0, 1000, 10))
    monkeypatch.setattr("gpuai_sdk.jobs._client.time.monotonic", lambda: next(clock))
    jobs = JobsClient()
    with pytest.raises(JobTimeout):
        jobs.run(["sleep", "999"], gpu_type="a100_80gb", timeout=25, on_output=None)
    assert api.jobs["job_1"]["status"] == "cancelled"


def test_list_walks_every_page_and_filters(api):
    jobs = JobsClient()
    for _ in range(5):
        jobs.submit(["true"], gpu_type="a100_80gb")
    ids = [j.id for j in jobs.list(page_size=2)]
    assert ids == ["job_5", "job_4", "job_3", "job_2", "job_1"]
    jobs.cancel("job_2")
    assert [j.id for j in jobs.list(status="cancelled")] == ["job_2"]


def test_gpu_types_and_trial_are_typed(api):
    jobs = JobsClient()
    types = jobs.gpu_types()
    assert types.complete is True
    assert types.data[0].gpu_type == "a100_80gb"
    assert types.data[0].price_per_gpu_hour == 1.29
    trial = jobs.trial()
    assert trial.eligible and trial.remaining_cents == 2500


def test_unknown_job_raises_not_found(api):
    with pytest.raises(gpuai_sdk.exceptions.NotFoundException):
        JobsClient().get("job_missing")


def _finished_job(api, jobs, files=None):
    job = jobs.submit(["true"], gpu_type="a100_80gb", image="busybox")
    jobs.wait(job.id)
    if files is not None:
        api.outputs[job.id] = _zip(files)
    return job


def test_outputs_is_pending_while_the_job_runs(api):
    jobs = JobsClient()
    job = jobs.submit(["true"], gpu_type="a100_80gb", image="busybox")
    out = jobs.outputs(job.id)
    assert out.status == "pending"
    with pytest.raises(JobOutputsUnavailable) as err:
        jobs.download_outputs(job.id)
    assert err.value.outputs.status == "pending"


def test_outputs_of_a_job_that_wrote_nothing_is_none(api):
    jobs = JobsClient()
    job = _finished_job(api, jobs)
    assert jobs.outputs(job.id).status == "none"
    with pytest.raises(JobOutputsUnavailable, match="none"):
        jobs.download_outputs(job.id)


def test_outputs_are_typed_with_the_download_link(api):
    jobs = JobsClient()
    job = _finished_job(api, jobs, {"result.txt": "ok"})
    out = jobs.outputs(job.id)
    assert out.status == "available"
    assert out.url.endswith(f"/blob/{job.id}")
    assert out.bytes == len(api.outputs[job.id])
    assert out.files[0].path == "result.txt"


def test_download_outputs_saves_the_zip_without_the_api_key(api, tmp_path):
    jobs = JobsClient()
    job = _finished_job(api, jobs, {"result.txt": "ok"})
    saved = jobs.download_outputs(job.id, tmp_path)
    assert saved == os.path.join(str(tmp_path), f"{job.id}-outputs.zip")
    with open(saved, "rb") as f:
        assert f.read() == api.outputs[job.id]
    assert not os.path.exists(saved + ".part")
    assert api.blob_auth == [None]

    named = jobs.download_outputs(job.id, tmp_path / "mine.zip")
    assert named == str(tmp_path / "mine.zip")


def test_download_outputs_extracts_into_a_directory(api, tmp_path):
    jobs = JobsClient()
    job = _finished_job(api, jobs, {"result.txt": "ok", "sub/metrics.json": "{}", "../escape.txt": "x"})
    dest = jobs.download_outputs(job.id, tmp_path / "out", extract=True)
    assert dest == str(tmp_path / "out")
    assert (tmp_path / "out" / "result.txt").read_text() == "ok"
    assert (tmp_path / "out" / "sub" / "metrics.json").read_text() == "{}"
    assert not (tmp_path / "escape.txt").exists()


def test_download_outputs_renews_an_expired_link_once(api, tmp_path):
    jobs = JobsClient()
    job = _finished_job(api, jobs, {"result.txt": "ok"})
    api.blob_fail = [403]
    saved = jobs.download_outputs(job.id, tmp_path)
    with open(saved, "rb") as f:
        assert f.read() == api.outputs[job.id]

    api.blob_fail = [403, 403]
    with pytest.raises(IOError, match="HTTP 403"):
        jobs.download_outputs(job.id, tmp_path / "again.zip")
    assert not (tmp_path / "again.zip").exists()


def test_upload_input_puts_the_file_and_returns_its_id(api, tmp_path):
    src = tmp_path / "clip.mp3"
    src.write_bytes(b"abc123")
    jobs = JobsClient()
    file_id = jobs.upload_input(src)
    assert file_id == "jfile_in1"
    assert api.bodies[-1] == {"filename": "clip.mp3", "bytes": 6}
    assert api.uploads["jfile_in1"] == b"abc123"
    assert api.blob_auth == [None]

    jobs.submit(["true"], gpu_type="a100_80gb", image="busybox", input_file=file_id)
    assert api.bodies[-1]["input_file"] == "jfile_in1"


def test_upload_input_refuses_an_empty_or_missing_file(api, tmp_path):
    empty = tmp_path / "empty"
    empty.write_bytes(b"")
    jobs = JobsClient()
    with pytest.raises(ValueError):
        jobs.upload_input(empty)
    with pytest.raises(ValueError):
        jobs.upload_input(tmp_path / "missing")
    assert api.bodies == []
