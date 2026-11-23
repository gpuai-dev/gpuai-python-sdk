"""JobsClient: submit a job, follow its output, wait for it to finish and
download the files it wrote.

A thin layer over the generated ``gpuai_sdk.JobsApi``. Every value it returns
is a generated model (``gpuai_sdk.Job``, ``gpuai_sdk.JobGpuTypes`` and so on),
and every refusal from the API is the generated ``gpuai_sdk.ApiException``.
What it adds is what a queue worker would otherwise write by hand: reading the
key from the environment, a safe retry of the submit, a log reader that
follows the job across polls, and a wait with a timeout.
"""

from __future__ import annotations

import json
import os
import shutil
import tempfile
import time
import uuid
import zipfile
from datetime import datetime, timezone
from typing import Any, Callable, Dict, Iterator, List, Mapping, Optional, Sequence, Union

import urllib3

from gpuai_sdk.api.jobs_api import JobsApi
from gpuai_sdk.api_client import ApiClient
from gpuai_sdk.configuration import Configuration
from gpuai_sdk.exceptions import ApiException
from gpuai_sdk.models.job import Job
from gpuai_sdk.models.job_create import JobCreate
from gpuai_sdk.models.job_create_repo import JobCreateRepo
from gpuai_sdk.models.job_gpu_types import JobGpuTypes
from gpuai_sdk.models.job_input_create import JobInputCreate
from gpuai_sdk.models.job_outputs import JobOutputs
from gpuai_sdk.models.job_telemetry import JobTelemetry
from gpuai_sdk.models.job_trial import JobTrial

DEFAULT_API_BASE = "https://api.gpu.ai/v1"

#: Job statuses after which a job never changes again.
TERMINAL_STATUSES = frozenset({"succeeded", "failed", "cancelled"})

# Output is uploaded from the machine every few seconds, so the last chunk can
# land shortly after the job is marked finished. stream_logs keeps reading for
# this long after a terminal status before it stops.
_LOG_SETTLE_SECONDS = 6.0


class JobFailed(Exception):
    """``wait(..., raise_on_failure=True)`` saw the job fail or be cancelled.

    Attributes:
        job: the finished ``gpuai_sdk.Job``; ``status``, ``status_reason`` and
            ``exit_code`` say what happened.
    """

    def __init__(self, job: Job):
        self.job = job
        reason = f": {job.status_reason}" if job.status_reason else ""
        code = f" (exit code {job.exit_code})" if job.exit_code is not None else ""
        super().__init__(f"job {job.id} {job.status}{code}{reason}")


class JobTimeout(TimeoutError):
    """``wait`` or ``stream_logs`` gave up before the job finished.

    The job itself keeps running; cancel it with ``JobsClient.cancel`` if it
    should stop. Attributes:
        job: the last ``gpuai_sdk.Job`` read.
    """

    def __init__(self, job: Job, timeout: float):
        self.job = job
        super().__init__(f"job {job.id} still {job.status} after {timeout:g}s")


class JobOutputsUnavailable(Exception):
    """``download_outputs`` found no archive to download.

    Attributes:
        outputs: the ``gpuai_sdk.JobOutputs`` read. Its ``status`` is
            ``pending`` (the job has not ended), ``none`` (it wrote nothing to
            /outputs) or ``expired`` (stored outputs are kept for 7 days), and
            ``message`` says the same in words.
    """

    def __init__(self, job_id: str, outputs: JobOutputs):
        self.outputs = outputs
        super().__init__(f"job {job_id} outputs are {outputs.status}: {outputs.message}")


def _retryable(err: BaseException) -> bool:
    """Whether a call that failed this way is safe and worth repeating."""
    if isinstance(err, urllib3.exceptions.HTTPError):
        return True
    if isinstance(err, ApiException):
        status = err.status or 0
        if status == 429 or status >= 500:
            return True
        if status == 409:
            # The first attempt of an idempotent request is still being
            # processed; repeating it returns that attempt's answer.
            try:
                return json.loads(err.body or "{}").get("code") == "idempotency_conflict"
            except (TypeError, ValueError):
                return False
    return False


def _finished_long_ago(job: Job) -> bool:
    """Whether the job finished more than the settle window ago, so its output
    is already complete and there is nothing left to wait for."""
    finished = job.finished_at
    if finished is None:
        return False
    if finished.tzinfo is None:
        finished = finished.replace(tzinfo=timezone.utc)
    # A minute, not the settle window itself, so a client clock running a few
    # seconds fast cannot cut off output that is still being uploaded.
    return (datetime.now(timezone.utc) - finished).total_seconds() > 60


class JobsClient:
    """Submit and follow GPU.ai jobs.

    The API key and base URL default to the ``GPUAI_API_KEY`` and
    ``GPUAI_API_BASE`` environment variables (``https://api.gpu.ai/v1`` when
    unset); values passed here win. Pass ``api_client`` instead to reuse an
    existing ``gpuai_sdk.ApiClient``.

    The generated API is at ``client.api`` (a ``gpuai_sdk.JobsApi``) for
    anything this class does not wrap.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        *,
        api_client: Optional[ApiClient] = None,
        retries: int = 4,
    ):
        if api_client is None:
            key = api_key or os.environ.get("GPUAI_API_KEY")
            if not key:
                raise ValueError(
                    "No API key. Set the GPUAI_API_KEY environment variable or pass api_key=... to JobsClient."
                )
            host = (api_base or os.environ.get("GPUAI_API_BASE") or DEFAULT_API_BASE).rstrip("/")
            api_client = ApiClient(Configuration(host=host, access_token=key))
        self.api_client = api_client
        self.api = JobsApi(api_client)
        self.retries = max(0, int(retries))

    def close(self) -> None:
        self.api_client.close()

    def __enter__(self) -> "JobsClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    # -- calls -------------------------------------------------------------

    def _call(self, fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Run one generated call, repeating it on 429, 5xx and network errors."""
        delay = 0.5
        for attempt in range(self.retries + 1):
            try:
                return fn(*args, **kwargs)
            except Exception as err:  # noqa: BLE001 - filtered by _retryable
                if attempt >= self.retries or not _retryable(err):
                    raise
                retry_after = None
                if isinstance(err, ApiException) and err.headers:
                    try:
                        retry_after = float(err.headers.get("Retry-After"))
                    except (TypeError, ValueError):
                        retry_after = None
                time.sleep(min(retry_after if retry_after is not None else delay, 30.0))
                delay = min(delay * 2, 8.0)
        raise AssertionError("unreachable")  # pragma: no cover

    def submit(
        self,
        command: Optional[Union[Sequence[str], str]] = None,
        *,
        gpu_type: Optional[str] = None,
        image: Optional[str] = None,
        script: Optional[str] = None,
        repo: Optional[Union[str, Mapping[str, str], JobCreateRepo]] = None,
        env: Optional[Mapping[str, str]] = None,
        name: Optional[str] = None,
        secrets: Optional[Sequence[str]] = None,
        idempotency_key: Optional[str] = None,
        **options: Any,
    ) -> Job:
        """Submit a job (POST /v1/jobs) and return it, usually ``queued``.

        ``command`` is the program and its arguments, as a list
        (``["python", "eval.py"]``); a single string is split on whitespace.
        Send ``script`` (a shell script) instead where the deployment runs a
        default image. ``repo`` is an https git URL, or ``{"url": ..., "ref":
        ...}``, to clone and run in. Any other ``POST /v1/jobs`` field
        (``timeout_seconds``, ``max_price_per_hour``, ``memory_hint_mb``,
        ``allow_sharing`` ...) goes in ``options`` by its API name.

        The submit carries an ``Idempotency-Key`` (a fresh one unless you pass
        your own), so a retried request never starts the job twice. Pass a key
        derived from your own work item id to make resubmits of the same item
        safe across processes too.
        """
        if isinstance(command, str):
            command = command.split()
        if isinstance(repo, str):
            repo = JobCreateRepo(url=repo)
        elif isinstance(repo, Mapping):
            repo = JobCreateRepo(**repo)
        fields: Dict[str, Any] = {
            "command": list(command) if command is not None else None,
            "gpu_type": gpu_type,
            "image": image,
            "script": script,
            "repo": repo,
            "env": dict(env) if env is not None else None,
            "name": name,
            "secrets": list(secrets) if secrets is not None else None,
        }
        fields.update(options)
        body = JobCreate(**{k: v for k, v in fields.items() if v is not None})
        key = idempotency_key or uuid.uuid4().hex
        return self._call(self.api.create_job, body, idempotency_key=key)

    def get(self, job_id: str) -> Job:
        """Read a job (GET /v1/jobs/{id}), including its attempts."""
        return self._call(self.api.get_job, job_id)

    def list(self, status: Optional[str] = None, *, page_size: int = 100) -> Iterator[Job]:
        """Yield this organization's jobs, newest first, across every page.

        ``status`` is one of queued, assigned, running, succeeded, failed or
        cancelled.
        """
        cursor: Optional[str] = None
        while True:
            page = self._call(self.api.list_jobs, status=status, cursor=cursor, limit=page_size)
            yield from page.data
            cursor = page.next_cursor
            if not cursor:
                return

    def cancel(self, job_id: str) -> Job:
        """Cancel a job. A running job stops within a few seconds."""
        return self._call(self.api.cancel_job, job_id, idempotency_key=uuid.uuid4().hex)

    def gpu_types(self) -> JobGpuTypes:
        """The GPU types jobs can run on, with the current price per GPU-hour.

        When ``complete`` is true, ``submit`` refuses any other ``gpu_type``.
        """
        return self._call(self.api.list_job_gpu_types)

    def trial(self) -> JobTrial:
        """Whether this organization's first jobs are free, and how much is left."""
        return self._call(self.api.get_job_trial)

    def telemetry(self, job_id: str) -> JobTelemetry:
        """The job's GPU memory and utilization over time."""
        return self._call(self.api.get_job_telemetry, job_id)

    # -- files -------------------------------------------------------------

    def outputs(self, job_id: str) -> JobOutputs:
        """What the job wrote to /outputs (GET /v1/jobs/{id}/outputs).

        ``status`` is ``available`` when there is a zip archive to download
        from ``url`` (a link valid for 15 minutes; call again for a fresh
        one), ``pending`` while the job runs, ``none`` when it wrote nothing
        and ``expired`` after 7 days. ``bytes`` and ``files`` describe the
        archive.
        """
        return self._call(self.api.get_job_outputs, job_id)

    def download_outputs(
        self,
        job_id: str,
        path: Optional[Union[str, "os.PathLike[str]"]] = None,
        *,
        extract: bool = False,
    ) -> str:
        """Download the job's outputs archive and return where it was saved.

        Without ``extract`` the zip is saved to ``path``: a file name, or an
        existing directory to save it in under the archive's own name (the
        current directory when ``path`` is omitted). With ``extract=True`` the
        archive's files are unpacked into the directory ``path`` (default
        ``<job-id>-outputs``), which is created if needed, and that directory
        is returned.

        Raises ``JobOutputsUnavailable`` when there is no archive (the job is
        still running, wrote nothing, or its outputs expired). Wait for the
        job first, e.g. with ``wait`` or ``run``.
        """
        info = self.outputs(job_id)
        if info.status != "available" or not info.url:
            raise JobOutputsUnavailable(job_id, info)
        name = os.path.basename(info.filename or "") or f"{job_id}-outputs.zip"
        if extract:
            dest_dir = os.fspath(path) if path is not None else f"{job_id}-outputs"
            os.makedirs(dest_dir, exist_ok=True)
            with tempfile.TemporaryDirectory() as tmp:
                archive = os.path.join(tmp, name)
                self._fetch(job_id, info, archive)
                with zipfile.ZipFile(archive) as zf:
                    # extractall drops absolute paths and ".." parts, so no
                    # member can land outside dest_dir.
                    zf.extractall(dest_dir)
            return dest_dir
        dest = os.fspath(path) if path is not None else name
        if os.path.isdir(dest):
            dest = os.path.join(dest, name)
        self._fetch(job_id, info, dest)
        return dest

    def _fetch(self, job_id: str, info: JobOutputs, dest: str) -> None:
        """Save the archive at ``info.url`` to ``dest``. The download link is
        presigned, so no API key is sent with it; a link that expired before
        the request is renewed once."""
        pool = self.api_client.rest_client.pool_manager
        url = info.url
        for attempt in range(2):
            resp = pool.request("GET", url, preload_content=False, redirect=True)
            try:
                if resp.status == 403 and attempt == 0:
                    fresh = self.outputs(job_id)
                    if fresh.status == "available" and fresh.url:
                        url = fresh.url
                        continue
                if resp.status != 200:
                    raise IOError(f"downloading the outputs of job {job_id}: HTTP {resp.status}")
                part = dest + ".part"
                try:
                    with open(part, "wb") as out:
                        shutil.copyfileobj(resp, out, 1 << 20)
                    os.replace(part, dest)
                except BaseException:
                    if os.path.exists(part):
                        os.remove(part)
                    raise
                return
            finally:
                resp.release_conn()

    def upload_input(self, path: Union[str, "os.PathLike[str]"]) -> str:
        """Upload a local file for a job to read and return its id.

        Pass the id as ``input_file`` to ``submit`` (or ``run``); the job
        downloads the file from ``GPUAI_INPUT_URL``. A file no job has read
        is deleted after 7 days.
        """
        path = os.fspath(path)
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            raise ValueError(f"{path} is not a non-empty file")
        size = os.path.getsize(path)
        created = self._call(
            self.api.create_job_input,
            JobInputCreate(filename=os.path.basename(path), bytes=size),
        )
        pool = self.api_client.rest_client.pool_manager
        with open(path, "rb") as body:
            resp = pool.request(
                "PUT",
                created.upload_url,
                body=body,
                headers={"Content-Length": str(size)},
                preload_content=True,
            )
        if resp.status // 100 != 2:
            raise IOError(f"uploading {path}: HTTP {resp.status}")
        return created.id

    # -- output ------------------------------------------------------------

    def _read_chunks(self, job_id: str, after: int) -> tuple[List[str], int]:
        """Read every chunk after ``after``; return their texts and the new cursor."""
        texts: List[str] = []
        while True:
            page = self._call(self.api.get_job_logs, job_id, after=after, limit=500)
            texts.extend(c.text for c in page.data)
            if not page.data or page.next_after <= after:
                return texts, after
            after = page.next_after

    def logs(self, job_id: str) -> str:
        """All of the job's output stored so far, as one string.

        Standard output and standard error are combined, across every
        attempt. Stored output is capped at about 8 MB per attempt.
        """
        texts, _ = self._read_chunks(job_id, 0)
        return "".join(texts)

    def stream_logs(
        self,
        job_id: str,
        *,
        poll_interval: float = 2.0,
        timeout: Optional[float] = None,
    ) -> Iterator[str]:
        """Yield the job's output as it arrives, until the job has finished.

        Each item is a piece of text as uploaded from the machine (not
        necessarily a whole line). The generator returns once the job is in a
        terminal status and its last output has been read. Raises
        ``JobTimeout`` after ``timeout`` seconds; the job keeps running.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        after = 0
        settle_until: Optional[float] = None
        while True:
            job = self.get(job_id)
            texts, after = self._read_chunks(job_id, after)
            yield from texts
            if job.status in TERMINAL_STATUSES:
                if _finished_long_ago(job):
                    return
                now = time.monotonic()
                if settle_until is None:
                    settle_until = now + _LOG_SETTLE_SECONDS
                if now >= settle_until:
                    return
            if deadline is not None and time.monotonic() >= deadline:
                raise JobTimeout(job, timeout or 0.0)
            time.sleep(poll_interval)

    def wait(
        self,
        job_id: str,
        *,
        timeout: Optional[float] = None,
        poll_interval: float = 3.0,
        raise_on_failure: bool = False,
    ) -> Job:
        """Poll until the job is succeeded, failed or cancelled; return it.

        Raises ``JobTimeout`` after ``timeout`` seconds (the job keeps
        running), and ``JobFailed`` for a failed or cancelled job when
        ``raise_on_failure`` is true.
        """
        deadline = None if timeout is None else time.monotonic() + timeout
        while True:
            job = self.get(job_id)
            if job.status in TERMINAL_STATUSES:
                if raise_on_failure and job.status != "succeeded":
                    raise JobFailed(job)
                return job
            if deadline is not None and time.monotonic() >= deadline:
                raise JobTimeout(job, timeout or 0.0)
            time.sleep(poll_interval)

    def run(
        self,
        command: Optional[Union[Sequence[str], str]] = None,
        *,
        on_output: Optional[Callable[[str], Any]] = print,
        timeout: Optional[float] = None,
        raise_on_failure: bool = True,
        poll_interval: float = 2.0,
        **submit_args: Any,
    ) -> Job:
        """Submit a job, pass its output to ``on_output`` as it arrives, and
        return the finished job.

        ``on_output`` defaults to printing each piece of output; pass
        ``None`` to only wait. The arguments are those of ``submit``. Raises
        ``JobFailed`` if the job does not succeed (unless
        ``raise_on_failure=False``) and ``JobTimeout`` after ``timeout``
        seconds, in which case the job is cancelled first.
        """
        job = self.submit(command, **submit_args)
        try:
            if on_output is None:
                done = self.wait(job.id, timeout=timeout, poll_interval=poll_interval)
            else:
                emit = (lambda text: on_output(text, end="")) if on_output is print else on_output
                for text in self.stream_logs(job.id, poll_interval=poll_interval, timeout=timeout):
                    emit(text)
                done = self.get(job.id)
        except JobTimeout:
            self.cancel(job.id)
            raise
        if raise_on_failure and done.status != "succeeded":
            raise JobFailed(done)
        return done
