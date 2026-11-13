"""Exceptions raised by gpuai_sdk.functions."""

from __future__ import annotations

from typing import Optional


class GPUAIError(Exception):
    """Base class for every error this library raises."""


class ConfigurationError(GPUAIError):
    """The library is not configured (for example, no API key)."""


class SerializationError(GPUAIError):
    """A function, its arguments or its result could not be pickled."""


class APIError(GPUAIError):
    """The GPU.ai API refused a request.

    Attributes:
        status: HTTP status code.
        code: stable error code from the API (for example ``validation_failed``).
        detail: the API's explanation.
        request_id: id to quote to support.
    """

    def __init__(self, status: int, code: str, detail: str, request_id: Optional[str] = None):
        self.status = status
        self.code = code
        self.detail = detail
        self.request_id = request_id
        suffix = f" (request {request_id})" if request_id else ""
        super().__init__(f"{detail} [{status} {code}]{suffix}")


class AuthenticationError(APIError):
    """The API key is missing, invalid, or lacks the ``functions`` scope."""


class InsufficientBalanceError(APIError):
    """The organization has no balance to start a machine with."""


class RemoteError(GPUAIError):
    """A call did not return a result.

    Raised by ``.remote()`` and ``RunHandle.result()``. When the function
    itself raised, ``type`` is the remote exception's class name (for example
    ``ValueError`` or ``torch.cuda.OutOfMemoryError``), ``message`` is its
    message and ``traceback`` is the remote traceback as text. When the
    platform ended the call, ``type`` names why: ``Timeout``, ``Cancelled``,
    ``LaunchError`` (no machine could be started), ``MachineLost``,
    ``DependencyError`` (pip failed), and so on.

    Attributes:
        type: name of the remote exception class, or the platform's reason.
        message: the remote exception's message.
        traceback: the remote traceback, or ``""``.
        status: the run's final status (``failed``, ``timed_out``, ``cancelled``).
        run_id: the run's id.
    """

    def __init__(self, type: str, message: str, traceback: str = "", status: str = "failed", run_id: str = ""):
        self.type = type
        self.message = message
        self.traceback = traceback
        self.status = status
        self.run_id = run_id
        super().__init__(f"{type}: {message}" if message else type)

    def __str__(self) -> str:
        base = super().__str__()
        if self.traceback:
            return f"{base}\n\nRemote traceback:\n{self.traceback.rstrip()}"
        return base


class RemoteTimeout(RemoteError, TimeoutError):
    """The call ran longer than the function's ``timeout`` and was stopped."""


class RemoteCancelled(RemoteError):
    """The call was cancelled before it returned."""


class ResultTimeout(GPUAIError, TimeoutError):
    """``RunHandle.result(timeout=...)`` gave up waiting.

    The call itself is still running; ask again or cancel it.
    """
