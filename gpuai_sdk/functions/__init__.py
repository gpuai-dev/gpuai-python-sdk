"""Run a Python function on a GPU.ai GPU by calling it.

    from gpuai_sdk.functions import function

    @function(gpu="a100_80gb", pip=["torch"])
    def gpu_name():
        import torch
        return torch.cuda.get_device_name(0)

    print(gpu_name.remote())

Set ``GPUAI_API_KEY`` first. See https://gpu.ai/docs/functions.

Hand-written, not generated: this subpackage is listed in
sdk/python/.openapi-generator-ignore so ``make sdk-generate`` never touches
it. It uses only the standard library and cloudpickle, and talks to the
/v1/functions endpoints directly (the pickled payloads those endpoints carry
are not something the generated client can model).
"""

import sys as _sys

if _sys.version_info < (3, 10):  # pragma: no cover - exercised on 3.9 only
    raise ImportError(
        "gpuai_sdk.functions requires Python 3.10 or newer (this is Python "
        f"{_sys.version_info[0]}.{_sys.version_info[1]}). Upgrade Python to use GPU.ai Functions."
    )

from ._client import configure
from ._function import Function, RunHandle, function
from ._imports import MissingPackageWarning
from .errors import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    GPUAIError,
    InsufficientBalanceError,
    RemoteCancelled,
    RemoteError,
    RemoteTimeout,
    ResultTimeout,
    SerializationError,
)

__all__ = [
    "function",
    "Function",
    "RunHandle",
    "configure",
    "GPUAIError",
    "APIError",
    "AuthenticationError",
    "ConfigurationError",
    "InsufficientBalanceError",
    "RemoteError",
    "RemoteTimeout",
    "RemoteCancelled",
    "ResultTimeout",
    "SerializationError",
    "MissingPackageWarning",
]
