"""Unit tests for the library against a small in-process fake of the API.

The fake stores versions and runs in memory and "executes" a run by loading
the uploaded pickle and calling it, which is what the machine's runner does.
The real service and the real runner are covered by the repository's
end-to-end test (`make test-e2e-functions`).
"""

import base64
import json
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cloudpickle
import pytest

import gpuai_sdk.functions as fn_lib
from gpuai_sdk.functions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    InsufficientBalanceError,
    RemoteCancelled,
    RemoteError,
    RemoteTimeout,
    ResultTimeout,
    SerializationError,
    function,
)


class FakeAPI:
    def __init__(self):
        self.functions = {}  # name -> id
        self.versions = {}  # id -> dict
        self.bundles = {}  # version id -> bytes
        self.runs = {}  # id -> dict
        self.requests = []  # (method, path, idempotency key)
        self.fail_next = []  # status codes to return before serving
        self.hold = False  # leave new runs queued
        self.balance = True
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), self._handler())
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    @property
    def base(self):
        return f"http://127.0.0.1:{self.server.server_address[1]}/v1"

    def count(self, method, suffix):
        return sum(1 for m, p, _ in self.requests if m == method and p.split("?")[0].endswith(suffix))

    def execute(self, run):
        version = self.versions[run["version_id"]]
        try:
            fn = cloudpickle.loads(self.bundles[version["id"]])
            args, kwargs = cloudpickle.loads(base64.b64decode(run["_input"]))
            run["_result"] = base64.b64encode(cloudpickle.dumps(fn(*args, **kwargs))).decode()
            run["status"] = "succeeded"
        except TimeoutError as e:
            run["status"] = "timed_out"
            run["error"] = {"type": "Timeout", "message": str(e)}
        except Exception as e:
            run["status"] = "failed"
            run["error"] = {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()}
        run["cost_usd"] = 0.0042

    def _handler(api):
        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _send(self, status, body=None):
                raw = json.dumps(body).encode() if body is not None else b""
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def _problem(self, status, code, detail):
                self._send(status, {"status": status, "code": code, "detail": detail, "request_id": "req_1"})

            def _serve(self, method):
                length = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(length) if length else b""
                path, _, query = self.path.partition("?")
                api.requests.append((method, self.path, self.headers.get("Idempotency-Key")))
                if path.startswith("/upload/"):
                    api.bundles[path.split("/")[-1]] = raw
                    return self._send(200)
                if self.headers.get("Authorization") != "Bearer test-key":
                    return self._problem(401, "invalid_api_key", "API key is invalid")
                if api.fail_next:
                    return self._problem(api.fail_next.pop(0), "internal_error", "try again")
                body = json.loads(raw) if raw else {}
                parts = path.split("/")[2:]  # after /v1
                if parts == ["functions"] and method == "POST":
                    fid = api.functions.setdefault(body["name"], f"fn-{len(api.functions) + 1}")
                    return self._send(200, {"id": fid, "name": body["name"]})
                if len(parts) == 3 and parts[2] == "versions":
                    for v in api.versions.values():
                        if v["content_hash"] == body["content_hash"]:
                            return self._send(200, {**v, "upload": None})
                    vid = f"ver-{len(api.versions) + 1}"
                    api.versions[vid] = {"id": vid, "status": "pending_upload", **body}
                    port = api.server.server_address[1]
                    upload = {"url": f"http://127.0.0.1:{port}/upload/{vid}", "method": "PUT"}
                    return self._send(201, {**api.versions[vid], "upload": upload})
                if len(parts) == 5 and parts[4] == "activate":
                    if parts[3] not in api.bundles:
                        return self._problem(422, "validation_failed", "bundle: not uploaded")
                    api.versions[parts[3]]["status"] = "ready"
                    return self._send(200, api.versions[parts[3]])
                if len(parts) == 3 and parts[2] == "runs" and method == "POST":
                    if not api.balance:
                        return self._problem(402, "insufficient_balance", "Insufficient balance.")
                    rid = f"run-{len(api.runs) + 1}"
                    run = {"id": rid, "function_id": parts[1], "version_id": body["version_id"], "status": "queued",
                           "error": None, "_input": body["input"]}
                    api.runs[rid] = run
                    if not api.hold:
                        api.execute(run)
                    return self._send(202, {k: v for k, v in run.items() if not k.startswith("_")})
                if len(parts) >= 4 and parts[2] == "runs":
                    run = api.runs.get(parts[3])
                    if run is None:
                        return self._problem(404, "not_found", "Run not found")
                    if len(parts) == 5 and parts[4] == "cancel":
                        if run["status"] == "queued":
                            run["status"] = "cancelled"
                            run["error"] = {"type": "Cancelled", "message": "The run was cancelled before it started."}
                    if len(parts) == 5 and parts[4] == "logs":
                        after = int(dict(q.split("=") for q in query.split("&") if q).get("after", 0))
                        data = [{"cursor": 1, "stream": "stdout", "data": "hello\n"},
                                {"cursor": 2, "stream": "stderr", "data": "warn\n"}][after:]
                        return self._send(200, {"data": data, "next_cursor": max(after, 2), "run_status": run["status"]})
                    out = {k: v for k, v in run.items() if not k.startswith("_")}
                    if "include_result=true" in query and run["status"] == "succeeded":
                        out["result"] = run["_result"]
                    return self._send(200, out)
                self._problem(404, "not_found", "no such route")

            def do_GET(self):
                self._serve("GET")

            def do_POST(self):
                self._serve("POST")

            def do_PUT(self):
                self._serve("PUT")

        return H


@pytest.fixture()
def api(monkeypatch):
    fake = FakeAPI()
    monkeypatch.setenv("GPUAI_API_KEY", "test-key")
    monkeypatch.setenv("GPUAI_API_BASE", fake.base)
    monkeypatch.setattr(fn_lib._client, "_config", {"api_key": None, "api_base": None})
    monkeypatch.setattr(fn_lib._client.time, "sleep", lambda s: None)
    yield fake
    fake.server.shutdown()


def test_direct_call_runs_locally_without_the_api(api):
    @function(gpu="a100_80gb")
    def add(a, b=1):
        return a + b

    assert add(2, b=3) == 5
    assert add.local(2) == 3
    assert add.__name__ == "add"
    assert api.requests == []


def test_remote_returns_the_result_and_deploys_once(api):
    @function(min_vram_gb=16, pip=["numpy"], timeout=30, idle_timeout=0, max_concurrency=3)
    def mul(a, b):
        return {"product": a * b}

    assert mul.remote(6, 7) == {"product": 42}
    assert mul.remote(2, b=5) == {"product": 10}
    assert api.count("POST", "/versions") == 1, "the second call must not redeploy"
    assert api.count("PUT", "/ver-1") == 1
    spec = api.versions["ver-1"]
    assert spec["pip"] == ["numpy"] and spec["timeout"] == 30 and spec["idle_timeout"] == 0
    assert spec["max_concurrency"] == 3 and spec["min_vram_gb"] == 16 and "gpu" not in spec
    assert spec["python_version"].startswith("3.") and spec["cloudpickle_version"] == cloudpickle.__version__
    assert len(spec["content_hash"]) == 64 and spec["bundle_bytes"] == len(api.bundles["ver-1"])


def test_same_code_and_settings_reuse_the_version_and_changes_make_a_new_one(api):
    def make(timeout):
        @function(name="same", timeout=timeout)
        def f():
            return 1

        return f

    make(30).remote()
    make(30).remote()
    assert len(api.versions) == 1 and api.count("PUT", "/ver-1") == 1, "an identical function must not upload again"
    make(31).remote()
    assert len(api.versions) == 2, "a changed setting is a new version"


def test_exception_in_the_function_becomes_remote_error(api):
    @function
    def explode(x):
        raise ValueError(f"bad input: {x}")

    with pytest.raises(RemoteError) as info:
        explode.remote(42)
    e = info.value
    assert e.type == "ValueError" and e.message == "bad input: 42" and e.status == "failed" and e.run_id == "run-1"
    assert "ValueError: bad input: 42" in e.traceback and "Remote traceback" in str(e)
    assert not isinstance(e, (RemoteTimeout, RemoteCancelled))


def test_timed_out_run_raises_remote_timeout(api):
    @function(timeout=1)
    def slow():
        raise TimeoutError("The run exceeded its 1 second timeout and was stopped.")

    with pytest.raises(RemoteTimeout) as info:
        slow.remote()
    assert isinstance(info.value, TimeoutError) and isinstance(info.value, RemoteError)
    assert info.value.status == "timed_out" and info.value.type == "Timeout"


def test_spawn_handle_status_result_timeout_cancel_logs(api):
    api.hold = True

    @function
    def job(x):
        return x + 1

    h = job.spawn(1)
    assert h.status() == "queued" and not h.done()
    with pytest.raises(ResultTimeout):
        h.result(timeout=0.01)
    assert h.logs() == "hello\nwarn\n"
    assert list(h.iter_logs()) == [("stdout", "hello\n"), ("stderr", "warn\n")]
    assert h.cancel() == "cancelled"
    with pytest.raises(RemoteCancelled):
        h.result()
    assert h.cancel() == "cancelled"

    h2 = job.spawn(1)
    api.execute(api.runs[h2.id])
    assert h2.result(timeout=5) == 2
    assert h2.info()["cost_usd"] == 0.0042 and h2.done()


def test_calls_are_retried_with_one_idempotency_key(api):
    @function
    def once():
        return "ok"

    once.deploy()
    api.requests.clear()
    api.fail_next = [503, 500]
    assert once.remote() == "ok"
    keys = [k for m, p, k in api.requests if m == "POST" and p.endswith("/runs")]
    assert len(keys) == 3 and len(set(keys)) == 1 and keys[0], "retries of one call must share one Idempotency-Key"
    assert len(api.runs) == 1


def test_api_errors_are_typed(api, monkeypatch):
    @function
    def f():
        return 1

    api.balance = False
    with pytest.raises(InsufficientBalanceError) as info:
        f.remote()
    assert info.value.status == 402 and info.value.code == "insufficient_balance" and info.value.request_id == "req_1"

    monkeypatch.setenv("GPUAI_API_KEY", "wrong")
    with pytest.raises(AuthenticationError):
        f.spawn()

    monkeypatch.delenv("GPUAI_API_KEY")
    with pytest.raises(ConfigurationError):
        f.spawn()

    fn_lib.configure(api_key="test-key")
    api.balance = True
    assert f.remote() == 1


def test_settings_are_validated_before_any_request(api):
    with pytest.raises(ValueError):
        function(name="has spaces")(lambda: 1)
    with pytest.raises(ValueError):
        function(lambda: 1)  # "<lambda>" is not a usable name
    with pytest.raises(TypeError):
        function(pip="numpy")(len)
    with pytest.raises(ValueError):
        function(pip=["--index-url=https://example.invalid"], name="x")(len)
    with pytest.raises(ValueError):
        function(timeout=0, name="x")(len)
    with pytest.raises(ValueError):
        function(max_concurrency=0, name="x")(len)
    assert api.requests == []


def test_unpicklable_things_fail_clearly(api):
    lock = threading.Lock()

    @function
    def captures():
        return lock.locked()

    with pytest.raises(SerializationError):
        captures.remote()

    @function
    def echo(x):
        return x

    with pytest.raises(SerializationError):
        echo.remote(lock)
    with pytest.raises(SerializationError) as info:
        echo.remote(b"x" * (4 * 1024 * 1024 + 1))
    assert "by reference" in str(info.value)
    assert not api.runs


def test_a_function_that_refers_to_its_decorated_self_needs_no_library_remotely(api):
    @function
    def fact(n):
        return 1 if n <= 1 else n * fact(n - 1)

    assert fact.remote(5) == 120
    # The pickle must not name this package: the machine does not have it.
    assert b"gpuai_sdk" not in api.bundles["ver-1"]


def test_deleted_function_is_redeployed_once(api):
    @function
    def f():
        return "again"

    assert f.remote() == "again"
    api.fail_next = [404]
    assert f.remote() == "again"
    assert api.count("POST", "/functions") == 2


def test_map_runs_every_item_in_order(api):
    @function
    def double(x):
        return x * 2

    assert double.map([1, 2, 3]) == [2, 4, 6]


def test_upload_failure_is_reported(api, monkeypatch):
    def refuse(*a, **k):
        raise APIError(403, "upload_failed", "Uploading the function's code failed with HTTP 403.")

    monkeypatch.setattr(fn_lib._client, "upload", refuse)

    @function
    def f():
        return 1

    with pytest.raises(APIError):
        f.remote()
    assert not api.runs
