"""The @function decorator, the Function it returns, and RunHandle."""

from __future__ import annotations

import base64
import copy
import functools
import hashlib
import json
import re
import sys
import threading
import time
from typing import Any, Callable, Dict, Iterator, List, Optional, Sequence, Tuple, Union

import cloudpickle

from . import _client
from .errors import (
    GPUAIError,
    RemoteCancelled,
    RemoteError,
    RemoteTimeout,
    ResultTimeout,
    SerializationError,
)

_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,62}$")
_SECRET_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,127}$")
_FINAL = ("succeeded", "failed", "timed_out", "cancelled")
# How long one "wait for this run" request is held by the API.
_WAIT_SECONDS = 25
MAX_INPUT_BYTES = 4 * 1024 * 1024

# Progress lines (``.remote()`` only). The first wait is short so a warm call
# that finishes at once prints nothing; after that, poll often enough to see
# each status change, and repeat the current one every minute.
_PROGRESS_FIRST_WAIT = 3
_PROGRESS_WAIT = 10
_PROGRESS_REPEAT_SECONDS = 60
_PROGRESS_TEXT = {
    "queued": "waiting for a GPU machine. A first call usually takes 2 to 4 minutes (up to about 10 on a slow host)",
    "setting_up": "the machine is up; installing Python and the pip requirements",
    "running": "running",
}
_PROGRESS_STILL = {"queued": "waiting for a machine", "setting_up": "installing", "running": "running"}


def _elapsed(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60}m {seconds % 60:02d}s" if seconds >= 60 else f"{seconds}s"


class _Progress:
    """Prints one stderr line per status change of a call, so a cold start
    that takes minutes does not look like a hang."""

    def __init__(self, handle: "RunHandle"):
        self.handle = handle
        self.started = time.monotonic()
        self.last_status: Optional[str] = None
        self.last_print = 0.0
        self.polls = 0
        self.printed = False

    def next_wait(self, wait: int) -> int:
        self.polls += 1
        return min(wait, _PROGRESS_FIRST_WAIT if self.polls == 1 else _PROGRESS_WAIT)

    def _print(self, text: str) -> None:
        # Progress is a courtesy: it must never turn a call that works into an
        # exception, and never land on stdout. With no stderr (pythonw, some
        # daemons) print(file=None) would write to stdout, so skip it; a closed
        # or broken stderr (a pipe whose reader exited) is ignored the same way.
        stream = sys.stderr
        if stream is not None:
            try:
                print(f"gpuai: {self.handle.name or 'function'}: {text}", file=stream, flush=True)
            except (OSError, ValueError):
                pass
        self.printed = True
        self.last_print = time.monotonic()

    def update(self, info: dict) -> None:
        status = info.get("status") or "queued"
        elapsed = time.monotonic() - self.started
        if status in _FINAL:
            if self.printed:
                self._print(f"{status} after {_elapsed(elapsed)}")
            return
        if status != self.last_status:
            text = _PROGRESS_TEXT.get(status, status)
            if self.last_status is None:
                url = _client.console_url(
                    f"/cloud/functions/{self.handle.function_id}/runs/{self.handle.id}"
                )
                if url:
                    text += f". Follow it at {url}"
            self._print(text)
            self.last_status = status
        elif time.monotonic() - self.last_print >= _PROGRESS_REPEAT_SECONDS:
            self._print(f"still {_PROGRESS_STILL.get(status, status)} ({_elapsed(elapsed)} so far)")


def _python_version() -> str:
    return f"{sys.version_info[0]}.{sys.version_info[1]}"


def _seconds(value: Union[int, float], what: str, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{what} must be a number of seconds")
    seconds = int(value)
    if seconds < minimum:
        raise ValueError(f"{what} must be at least {minimum} second(s)")
    return seconds


class RunHandle:
    """One call of a function, running or finished.

    Returned by ``Function.spawn()``. Nothing here blocks unless you ask it
    to: ``result()`` waits, the rest return at once.
    """

    def __init__(self, function_id: str, run_id: str, info: Optional[dict] = None, name: str = ""):
        self.function_id = function_id
        self.id = run_id
        self.name = name
        self._info: dict = info or {"id": run_id, "status": "queued"}

    def __repr__(self) -> str:
        return f"<RunHandle {self.id} {self._info.get('status', '?')}>"

    @property
    def _path(self) -> str:
        return f"/functions/{self.function_id}/runs/{self.id}"

    def info(self, refresh: bool = True) -> dict:
        """The run as the API describes it: status, timings, ``cost_usd``,
        ``cold_start``, ``error``."""
        if refresh and self._info.get("status") not in _FINAL:
            self._info = _client.request("GET", self._path)
        return dict(self._info)

    def status(self) -> str:
        """``queued`` (waiting for a machine), ``setting_up`` (installing
        Python and pip requirements on the machine), ``running``,
        ``succeeded``, ``failed``, ``timed_out`` or ``cancelled``."""
        return self.info()["status"]

    def done(self) -> bool:
        return self.status() in _FINAL

    def result(self, timeout: Optional[float] = None, progress: bool = False) -> Any:
        """Wait for the call and return what the function returned.

        Raises RemoteError (or its subclasses RemoteTimeout and
        RemoteCancelled) if the call did not succeed, and ResultTimeout if
        ``timeout`` seconds pass first. A ResultTimeout does not stop the
        call; use ``cancel()`` for that.

        With ``progress=True`` a line goes to stderr each time the call
        changes status (waiting for a machine, installing, running) and once
        a minute while it stays the same. ``.remote()`` turns this on unless
        ``GPUAI_PROGRESS=0``.
        """
        reporter = _Progress(self) if progress else None
        deadline = None if timeout is None else time.monotonic() + timeout
        while True:
            wait = reporter.next_wait(_WAIT_SECONDS) if reporter else _WAIT_SECONDS
            if deadline is not None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise ResultTimeout(f"run {self.id} did not finish within {timeout} seconds (it is still {self._info.get('status')})")
                wait = max(1, min(_WAIT_SECONDS, int(remaining + 0.999)))
            self._info = _client.request(
                "GET", f"{self._path}?wait={wait}&include_result=true", timeout=wait + 30
            )
            status = self._info.get("status")
            if reporter:
                reporter.update(self._info)
            if status in _FINAL:
                break
        if status == "succeeded":
            raw = base64.b64decode(self._info.pop("result", None) or "")
            try:
                return cloudpickle.loads(raw)
            except Exception as e:
                raise SerializationError(
                    f"The call succeeded but its result could not be unpickled here: {type(e).__name__}: {e}. "
                    "The result's type is probably defined in a package that is not installed on this computer."
                ) from e
        raise _error_for(self._info)

    def cancel(self) -> str:
        """Stop the call. Returns the run's status after the request: a queued
        call is ``cancelled`` at once, a running one within a few seconds.
        Cancelling a finished call does nothing."""
        self._info = _client.request("POST", self._path + "/cancel", {}, idempotent=True)
        return self._info["status"]

    def iter_logs(self, follow: bool = False) -> Iterator[Tuple[str, str]]:
        """Yield ``(stream, text)`` chunks of the call's output in order.

        ``stream`` is ``stdout``, ``stderr`` or ``system`` (platform messages
        such as dependency installation). With ``follow=True`` this keeps
        yielding until the call finishes.
        """
        cursor = 0
        while True:
            wait = f"&wait={_WAIT_SECONDS}" if follow else ""
            page = _client.request("GET", f"{self._path}/logs?after={cursor}{wait}", timeout=_WAIT_SECONDS + 30)
            for chunk in page["data"]:
                yield chunk["stream"], chunk["data"]
            cursor = page["next_cursor"]
            if page["data"]:
                continue  # there may be more already
            if not follow or page["run_status"] in _FINAL:
                return

    def logs(self) -> str:
        """Everything the call has printed so far, as one string."""
        return "".join(text for _, text in self.iter_logs())


def _error_for(info: dict) -> RemoteError:
    err = info.get("error") or {}
    status = info.get("status", "failed")
    kind = err.get("type") or {"timed_out": "Timeout", "cancelled": "Cancelled"}.get(status, "RunFailed")
    cls = {"timed_out": RemoteTimeout, "cancelled": RemoteCancelled}.get(status, RemoteError)
    return cls(kind, err.get("message", ""), err.get("traceback", ""), status, info.get("id", ""))


class Function:
    """A Python function that can also run on a GPU.ai GPU.

    Created by the ``@function`` decorator. Call it like the original
    function to run it here; use ``.remote()`` or ``.spawn()`` to run it on
    GPU.ai.
    """

    def __init__(
        self,
        fn: Callable[..., Any],
        *,
        name: Optional[str],
        gpu: Optional[str],
        min_vram_gb: Optional[int],
        gpu_count: int,
        pip: Sequence[str],
        timeout: Union[int, float],
        idle_timeout: Union[int, float],
        max_concurrency: int,
        regions: Optional[Sequence[str]],
        max_price_per_hour: Optional[float],
        include: Sequence[Any],
        secrets: Sequence[str] = (),
    ):
        if not callable(fn):
            raise TypeError("@function must decorate a function")
        self._fn = fn
        self.name = name or getattr(fn, "__name__", "")
        if not _NAME_RE.match(self.name):
            raise ValueError(
                f"{self.name!r} cannot be used as a function name. Pass name=..., starting with a letter and using "
                "only letters, digits, underscores and hyphens (63 characters at most)."
            )
        if isinstance(pip, str):
            raise TypeError('pip must be a list of requirements, for example pip=["numpy", "torch==2.5.1"]')
        self.pip: List[str] = [str(p) for p in pip]
        for req in self.pip:
            if req.startswith("-"):
                raise ValueError(f"pip options are not accepted ({req!r}); list package requirements only")
        self.gpu = gpu
        self.min_vram_gb = int(min_vram_gb) if min_vram_gb else 0
        self.gpu_count = int(gpu_count)
        self.timeout = _seconds(timeout, "timeout", 1)
        self.idle_timeout = _seconds(idle_timeout, "idle_timeout", 0)
        self.max_concurrency = int(max_concurrency)
        if self.max_concurrency < 1:
            raise ValueError("max_concurrency must be at least 1")
        self.regions: List[str] = list(regions or [])
        self.max_price_per_hour = max_price_per_hour
        if isinstance(secrets, str):
            raise TypeError('secrets must be a list of secret names, for example secrets=["HF_TOKEN"]')
        names = sorted({str(n).strip() for n in secrets})
        for n in names:
            if not _SECRET_NAME_RE.match(n) or n.upper().startswith("GPUAI_"):
                raise ValueError(
                    f"{n!r} is not a valid secret name. Secret names are environment variable names: a letter or "
                    "underscore, then letters, digits and underscores, not starting with GPUAI_."
                )
        self.secrets: List[str] = names
        self._include = list(include)
        self._lock = threading.Lock()
        self._deployed: Optional[Tuple[str, str]] = None  # (function_id, version_id)
        functools.update_wrapper(self, fn)

    # Pickling a Function (for example because the decorated function calls
    # itself, or another decorated function, by its module-level name) must
    # not drag this library onto the machine: there, it is the plain function.
    # copy.copy is the standard library's identity for functions, so the
    # pickle needs nothing from this package to load.
    def __reduce__(self):
        return (copy.copy, (self._fn,))

    def __repr__(self) -> str:
        return f"<gpuai_sdk.functions.Function {self.name}>"

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Run the function on this computer, exactly as if undecorated."""
        return self._fn(*args, **kwargs)

    def local(self, *args: Any, **kwargs: Any) -> Any:
        """Same as calling the function directly: run it here."""
        return self._fn(*args, **kwargs)

    # -- packaging ---------------------------------------------------------

    def _bundle(self) -> bytes:
        """Pickle the function by value, so its code travels with the call
        and the machine needs neither this file nor a container build."""
        modules = []
        mod_name = getattr(self._fn, "__module__", None)
        if mod_name and mod_name != "__main__" and mod_name in sys.modules:
            modules.append(sys.modules[mod_name])
        modules.extend(self._include)
        registered = []
        try:
            for mod in modules:
                try:
                    cloudpickle.register_pickle_by_value(mod)
                    registered.append(mod)
                except Exception:
                    pass  # already registered, or not a module cloudpickle can register
            return cloudpickle.dumps(self._fn)
        except Exception as e:
            raise SerializationError(
                f"The function {self.name!r} could not be pickled: {type(e).__name__}: {e}. Functions must not capture "
                "things that cannot be copied to another machine (open files, locks, database connections)."
            ) from e
        finally:
            for mod in registered:
                try:
                    cloudpickle.unregister_pickle_by_value(mod)
                except Exception:
                    pass

    def _spec(self, bundle: bytes) -> dict:
        spec: Dict[str, Any] = {
            "bundle_sha256": hashlib.sha256(bundle).hexdigest(),
            "bundle_bytes": len(bundle),
            "python_version": _python_version(),
            "cloudpickle_version": cloudpickle.__version__,
            "pip": self.pip,
            "gpu_count": self.gpu_count,
            "min_vram_gb": self.min_vram_gb,
            "regions": self.regions,
            "timeout": self.timeout,
            "idle_timeout": self.idle_timeout,
            "max_concurrency": self.max_concurrency,
        }
        if self.gpu:
            spec["gpu"] = self.gpu
        if self.max_price_per_hour is not None:
            spec["max_price_per_hour"] = float(self.max_price_per_hour)
        if self.secrets:
            # Only when set, so a function without secrets keeps the content
            # hash it had before this option existed.
            spec["secrets"] = self.secrets
        # The version is the code plus everything declared about it: change
        # either and the next call registers a new version.
        spec["content_hash"] = hashlib.sha256(json.dumps(spec, sort_keys=True).encode("utf-8")).hexdigest()
        return spec

    def deploy(self) -> str:
        """Register the function with GPU.ai and upload its code if GPU.ai
        does not already have this exact version. Returns the version id.

        You rarely need to call this: the first ``.remote()`` or ``.spawn()``
        does it. It starts no machine and costs nothing.
        """
        with self._lock:
            if self._deployed is None:
                bundle = self._bundle()
                spec = self._spec(bundle)
                fn = _client.request("POST", "/functions", {"name": self.name}, idempotent=True)
                version = _client.request("POST", f"/functions/{fn['id']}/versions", spec, idempotent=True)
                upload = version.get("upload")
                if upload:
                    _client.upload(upload["url"], bundle, upload.get("method", "PUT"))
                # Confirms the upload and makes this the function's current
                # version (its idle_timeout and max_concurrency apply).
                _client.request(
                    "POST", f"/functions/{fn['id']}/versions/{version['id']}/activate", {}, idempotent=True
                )
                self._deployed = (fn["id"], version["id"])
            return self._deployed[1]

    # -- calling -----------------------------------------------------------

    def spawn(self, *args: Any, **kwargs: Any) -> RunHandle:
        """Start a call on GPU.ai and return at once with a RunHandle."""
        try:
            payload = cloudpickle.dumps((args, kwargs))
        except Exception as e:
            raise SerializationError(f"The arguments could not be pickled: {type(e).__name__}: {e}") from e
        if len(payload) > MAX_INPUT_BYTES:
            raise SerializationError(
                f"The pickled arguments are {len(payload)} bytes; the limit is {MAX_INPUT_BYTES}. "
                "Pass large data by reference (a URL or an object-store key) and load it inside the function."
            )
        self.deploy()
        assert self._deployed is not None
        function_id, version_id = self._deployed
        body = {"version_id": version_id, "input": base64.b64encode(payload).decode("ascii")}
        try:
            run = _client.request("POST", f"/functions/{function_id}/runs", body, idempotent=True)
        except GPUAIError as e:
            # The function was deleted (or its version removed) since this
            # process deployed it: deploy again once and retry.
            if getattr(e, "status", None) != 404:
                raise
            with self._lock:
                self._deployed = None
            self.deploy()
            function_id, version_id = self._deployed  # type: ignore[misc]
            body["version_id"] = version_id
            run = _client.request("POST", f"/functions/{function_id}/runs", body, idempotent=True)
        return RunHandle(function_id, run["id"], run, name=self.name)

    def remote(self, *args: Any, **kwargs: Any) -> Any:
        """Run the function on GPU.ai and return its result.

        Blocks until the call finishes. If the function raises, this raises
        RemoteError carrying the remote exception's type, message and
        traceback. While it waits it prints a progress line to stderr when
        the call changes status, so a cold start does not look like a hang.
        Set ``GPUAI_PROGRESS=0`` (or ``configure(progress=False)``) to
        silence it.
        """
        return self.spawn(*args, **kwargs).result(progress=_client.progress_enabled())

    def map(self, inputs: Sequence[Any]) -> List[Any]:
        """Call the function once per item and return the results in order.

        Calls beyond ``max_concurrency`` wait in the queue. The first failure
        is raised after every call has finished.
        """
        handles = [self.spawn(item) for item in inputs]
        results, first_error = [], None
        for handle in handles:
            try:
                results.append(handle.result())
            except RemoteError as e:
                first_error = first_error or e
                results.append(None)
        if first_error is not None:
            raise first_error
        return results


def function(
    fn: Optional[Callable[..., Any]] = None,
    *,
    gpu: Optional[str] = None,
    min_vram_gb: Optional[int] = None,
    gpu_count: int = 1,
    pip: Sequence[str] = (),
    timeout: Union[int, float] = 600,
    idle_timeout: Union[int, float] = 300,
    max_concurrency: int = 1,
    name: Optional[str] = None,
    regions: Optional[Sequence[str]] = None,
    max_price_per_hour: Optional[float] = None,
    include: Sequence[Any] = (),
    secrets: Sequence[str] = (),
) -> Any:
    """Mark a function to run on a GPU.ai GPU.

    ::

        @function(gpu="a100_80gb", pip=["transformers"], timeout=600)
        def embed(texts):
            ...

        embed.remote(["hello"])   # runs on GPU.ai, returns the result
        embed.spawn(["hello"])    # runs in the background, returns a RunHandle
        embed(["hello"])          # runs here, as if undecorated

    Args:
        gpu: a GPU type from ``GET /v1/gpu-types`` (for example
            ``"a100_80gb"``). Omit it, with or without ``min_vram_gb``, to take
            the cheapest available GPU that fits.
        min_vram_gb: least VRAM per GPU, used when ``gpu`` is not given.
        gpu_count: GPUs on the machine (default 1).
        pip: Python requirements to install on the machine, as you would pass
            them to ``pip install``. Installed once per machine and cached.
        timeout: seconds one call may run before it is stopped (default 600).
        idle_timeout: seconds a machine stays ready after a call, so the next
            call skips machine start-up (default 300). You pay for this time.
            0 releases the machine as soon as the call returns.
        max_concurrency: most machines running calls at once (default 1).
            Calls beyond it wait in a queue.
        name: the function's name on GPU.ai (default: the Python name).
        regions: restrict placement to these region codes.
        max_price_per_hour: do not start a machine above this hourly price.
        include: extra local modules to ship with the function. The module
            the function is defined in is always shipped; helpers imported
            from your other local modules must be listed here.
        secrets: names of organization secrets (``gpu secrets set NAME``) to
            put in the function's environment, as ``os.environ["NAME"]``. The
            values are fetched for each call and never pass through this
            library. Every name must exist when the function is deployed.
    """

    def wrap(f: Callable[..., Any]) -> Function:
        return Function(
            f,
            name=name,
            gpu=gpu,
            min_vram_gb=min_vram_gb,
            gpu_count=gpu_count,
            pip=pip,
            timeout=timeout,
            idle_timeout=idle_timeout,
            max_concurrency=max_concurrency,
            regions=regions,
            max_price_per_hour=max_price_per_hour,
            include=include,
            secrets=secrets,
        )

    if fn is not None:  # used as a bare @function
        return wrap(fn)
    return wrap
