"""Quickstart: run one job on a GPU and print its output.

    pip install gpuai-sdk
    export GPUAI_API_KEY=gpuai_...
    python quickstart.py [gpu_type]

The job prints the GPU it was given and exits. The first job starts a machine,
usually in 3 to 10 minutes; the machine is shut down a few minutes after the
job ends, so the whole run costs a few cents.
"""

import sys

from gpuai_sdk.jobs import JobsClient


def main() -> None:
    jobs = JobsClient()

    types = jobs.gpu_types().data
    for t in types:
        price = f"${t.price_per_gpu_hour}/GPU-hour" if t.price_per_gpu_hour is not None else "not in stock now"
        print(f"{t.gpu_type:<14} {t.vram_gb:>4} GB  {price}")

    # Default to the cheapest type in stock; pass a gpu_type to pick one.
    in_stock = sorted((t for t in types if t.available_now), key=lambda t: t.price_per_gpu_hour)
    gpu_type = sys.argv[1] if len(sys.argv) > 1 else in_stock[0].gpu_type

    job = jobs.run(
        ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
        name="sdk-quickstart",
        gpu_type=gpu_type,
        image="nvidia/cuda:12.4.1-base-ubuntu22.04",
        timeout_seconds=300,
        timeout=1800,  # stop waiting (and cancel the job) after 30 minutes
    )
    print(f"{job.id}: {job.status}, exit code {job.exit_code}, cost ${job.attributed_cost_usd:.4f}")


if __name__ == "__main__":
    main()
