"""Example 2: use a pip dependency.

The function needs numpy. Listing it in pip=[...] is all it takes: GPU.ai
installs it on the machine before the first call and keeps it for later ones.
Nothing is installed on your computer beyond gpuai-sdk itself.

    export GPUAI_API_KEY=gpuai_...
    python 02_pip_dependency.py
"""

from gpuai_sdk.functions import function


@function(min_vram_gb=8, pip=["numpy>=1.26"], timeout=300)
def column_stats(rows):
    import numpy as np

    data = np.asarray(rows, dtype=np.float64)
    return {
        "numpy": np.__version__,
        "mean": data.mean(axis=0).round(4).tolist(),
        "std": data.std(axis=0).round(4).tolist(),
    }


if __name__ == "__main__":
    stats = column_stats.remote([[1, 10], [2, 20], [3, 30], [4, 40]])
    print("numpy on the machine:", stats["numpy"])
    print("mean:", stats["mean"])   # [2.5, 25.0]
    print("std: ", stats["std"])    # [1.118, 11.1803]
