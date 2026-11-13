"""Example 3: errors, timeouts, background calls and cancel.

Shows what the caller sees when things do not go to plan:

  1. an exception raised inside the function reaches the caller, with its
     type, message and remote traceback;
  2. a call that runs past its timeout is stopped;
  3. a background call can be watched and cancelled.

    export GPUAI_API_KEY=gpuai_...
    python 03_errors_timeouts_cancel.py
"""

import time

from gpuai_sdk.functions import RemoteCancelled, RemoteError, RemoteTimeout, function


@function(min_vram_gb=8, timeout=120)
def divide(a, b):
    return a / b


@function(min_vram_gb=8, timeout=5)
def too_slow():
    import time

    print("starting a 60 second job with a 5 second timeout")
    time.sleep(60)
    return "never returned"


@function(min_vram_gb=8, timeout=600)
def long_job(seconds):
    import time

    for i in range(seconds):
        print(f"step {i + 1} of {seconds}")
        time.sleep(1)
    return "finished"


if __name__ == "__main__":
    # 1. An error inside the function reaches the caller.
    print("divide(1, 0):")
    try:
        divide.remote(1, 0)
    except RemoteError as e:
        print("  type:   ", e.type)       # ZeroDivisionError
        print("  message:", e.message)    # division by zero
        print("  remote traceback ends with:", e.traceback.strip().splitlines()[-1])

    # 2. A call past its timeout is stopped, and stops costing run time.
    print("too_slow():")
    try:
        too_slow.remote()
    except RemoteTimeout as e:
        print("  stopped:", e.message)

    # 3. A background call: watch it, read its output, cancel it.
    print("long_job(300) in the background:")
    handle = long_job.spawn(300)
    while handle.status() in ("queued", "setting_up"):  # wait for the function body to start
        time.sleep(2)
    time.sleep(5)
    print("  status:", handle.status())
    print("  output so far:", handle.logs().strip().splitlines()[-1:])
    handle.cancel()
    try:
        handle.result(timeout=60)
    except RemoteCancelled:
        print("  cancelled; final status:", handle.status())
        print("  cost of the cancelled call: $%.4f" % (handle.info().get("cost_usd") or 0))
