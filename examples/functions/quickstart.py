"""Quickstart: run one function on a GPU.

    pip install gpuai-sdk
    export GPUAI_API_KEY=gpuai_...
    python quickstart.py

The first call starts a machine, usually in 1 to 2 minutes. The second call
reuses it and returns in about 2 seconds.
"""

from gpuai_sdk.functions import function


@function(min_vram_gb=16, idle_timeout=300)
def gpu_info():
    import subprocess

    out = subprocess.run(
        ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
        capture_output=True, text=True, check=True,
    )
    return out.stdout.strip()


if __name__ == "__main__":
    print("First call (starts a machine):", gpu_info.remote())
    print("Second call (machine is warm):", gpu_info.remote())
