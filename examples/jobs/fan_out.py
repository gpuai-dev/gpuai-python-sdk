"""Fan out: submit one job per shard, then collect every result.

    export GPUAI_API_KEY=gpuai_...
    python fan_out.py

The pattern for a queue worker. Each job gets an idempotency key derived from
its work item, so running this script twice (or retrying after a crash) does
not start a shard twice. Jobs from one organization that opt in to sharing
may run on the same GPU, so small shards do not each need a machine.
"""

from gpuai_sdk.jobs import JobsClient

SHARDS = 4
IMAGE = "ghcr.io/acme/eval:1.4"  # replace with your image


def main() -> None:
    jobs = JobsClient()

    ids = []
    for shard in range(SHARDS):
        job = jobs.submit(
            ["python", "eval.py", "--shard", str(shard), "--of", str(SHARDS)],
            name="eval-shard",
            image=IMAGE,
            gpu_type="a100_80gb",
            timeout_seconds=1800,
            memory_hint_mb=12000,
            allow_sharing=True,
            allow_restart=True,
            max_wait_seconds=600,
            idempotency_key=f"eval-2026-11-22-shard-{shard}",
        )
        ids.append(job.id)
        print("submitted", job.id)

    for job_id in ids:
        done = jobs.wait(job_id, timeout=3 * 3600)
        tail = jobs.logs(job_id).strip().splitlines()[-1:] or [""]
        print(f"{job_id} {done.status} exit={done.exit_code} ${done.attributed_cost_usd:.4f} {tail[0]}")


if __name__ == "__main__":
    main()
