"""Run work on a GPU.ai GPU as a job and get its output.

    from gpuai_sdk.jobs import JobsClient

    jobs = JobsClient()  # reads GPUAI_API_KEY
    job = jobs.run(["nvidia-smi"], gpu_type="a100_80gb", image="nvidia/cuda:12.4.1-base-ubuntu22.04")
    print(job.status, job.attributed_cost_usd)
    jobs.download_outputs(job.id, "results", extract=True)  # what it wrote to /outputs

A machine is started for each job and shut down a few minutes after it ends,
so nothing bills after the work is done. See https://gpu.ai/docs/guides/jobs.

Hand-written, not generated: this subpackage is listed in
sdk/python/.openapi-generator-ignore so ``make sdk-generate`` never touches
it. It wraps the generated ``gpuai_sdk.JobsApi`` and returns its models.
"""

from ._client import TERMINAL_STATUSES, JobFailed, JobOutputsUnavailable, JobsClient, JobTimeout

__all__ = ["JobsClient", "JobFailed", "JobTimeout", "JobOutputsUnavailable", "TERMINAL_STATUSES"]
