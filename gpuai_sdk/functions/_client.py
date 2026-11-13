"""A small HTTP client for the functions API. Standard library only."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
import uuid
from typing import Any, Dict, Optional

from .errors import APIError, AuthenticationError, ConfigurationError, InsufficientBalanceError

DEFAULT_API_BASE = "https://api.gpu.ai/v1"
_USER_AGENT = "gpuai-sdk-python-functions"

_config: Dict[str, Optional[str]] = {"api_key": None, "api_base": None}


def configure(api_key: Optional[str] = None, api_base: Optional[str] = None) -> None:
    """Set the API key and base URL in code.

    Both default to the environment: ``GPUAI_API_KEY`` and ``GPUAI_API_BASE``
    (``https://api.gpu.ai/v1`` when unset). Values passed here win.
    """
    if api_key is not None:
        _config["api_key"] = api_key
    if api_base is not None:
        _config["api_base"] = api_base


def _api_key() -> str:
    key = _config["api_key"] or os.environ.get("GPUAI_API_KEY")
    if not key:
        raise ConfigurationError(
            "No API key. Set the GPUAI_API_KEY environment variable, or call gpuai_sdk.functions.configure(api_key=...)."
        )
    return key


def _api_base() -> str:
    return (_config["api_base"] or os.environ.get("GPUAI_API_BASE") or DEFAULT_API_BASE).rstrip("/")


def _raise_for(status: int, body: bytes) -> None:
    code, detail, request_id = "error", "", None
    try:
        problem = json.loads(body.decode("utf-8"))
        code = problem.get("code") or code
        detail = problem.get("detail") or problem.get("title") or ""
        request_id = problem.get("request_id")
    except Exception:
        detail = body.decode("utf-8", "replace")[:500]
    if not detail:
        detail = f"HTTP {status}"
    if status in (401, 403):
        raise AuthenticationError(status, code, detail, request_id)
    if status == 402:
        raise InsufficientBalanceError(status, code, detail, request_id)
    raise APIError(status, code, detail, request_id)


def request(
    method: str,
    path: str,
    body: Optional[dict] = None,
    *,
    idempotent: bool = False,
    timeout: float = 60.0,
    retries: int = 4,
) -> Any:
    """Call the API and return the decoded JSON body (None for 204).

    GETs, and POSTs marked idempotent (they carry one Idempotency-Key for
    every attempt), are retried on network errors, 429 and 5xx. A 409
    ``idempotency_conflict`` means the first attempt is still being
    processed, so it is retried too and then returns that attempt's answer.
    """
    url = _api_base() + path
    headers = {"Authorization": "Bearer " + _api_key(), "User-Agent": _USER_AGENT, "Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if idempotent and method != "GET":
        headers["Idempotency-Key"] = uuid.uuid4().hex
    can_retry = method == "GET" or idempotent

    delay = 0.5
    attempt = 0
    while True:
        attempt += 1
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                return json.loads(raw.decode("utf-8")) if raw else None
        except urllib.error.HTTPError as e:
            raw = e.read()
            retryable = e.code == 429 or e.code >= 500 or (e.code == 409 and b"idempotency_conflict" in raw)
            if can_retry and retryable and attempt <= retries:
                retry_after = e.headers.get("Retry-After") if e.headers else None
                wait = delay
                if retry_after:
                    try:
                        wait = min(float(retry_after), 30.0)
                    except ValueError:
                        pass
                time.sleep(wait)
                delay = min(delay * 2, 8.0)
                continue
            _raise_for(e.code, raw)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if can_retry and attempt <= retries:
                time.sleep(delay)
                delay = min(delay * 2, 8.0)
                continue
            raise APIError(0, "network_error", f"Could not reach {_api_base()}: {e}") from e


def upload(url: str, data: bytes, method: str = "PUT", timeout: float = 300.0) -> None:
    """Upload a bundle to the presigned URL the API handed out."""
    last: Optional[Exception] = None
    for attempt in range(3):
        req = urllib.request.Request(
            url, data=data, method=method, headers={"Content-Type": "application/octet-stream", "User-Agent": _USER_AGENT}
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout):
                return
        except urllib.error.HTTPError as e:
            if e.code < 500:
                raise APIError(e.code, "upload_failed", f"Uploading the function's code failed with HTTP {e.code}.") from e
            last = e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
        time.sleep(1.0 * (attempt + 1))
    raise APIError(0, "upload_failed", f"Uploading the function's code failed: {last}")
