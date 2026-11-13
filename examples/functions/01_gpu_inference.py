"""Example 1: run a model on a GPU.

Loads a small sentiment model with PyTorch on the GPU and classifies a few
sentences. The model is loaded on the first call a machine serves and stays in
GPU memory, so later calls on that warm machine skip the load.

    export GPUAI_API_KEY=gpuai_...
    python 01_gpu_inference.py
"""

from gpuai_sdk.functions import function

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
_loaded = {}  # filled on the machine, on the first call it serves


@function(
    min_vram_gb=16,              # any GPU with at least 16 GB; or name one: gpu="a100_80gb"
    pip=["torch", "transformers>=4.44"],  # torch is already on the machine for Python 3.10
    timeout=600,
    idle_timeout=300,
)
def classify(texts):
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    if not torch.cuda.is_available():
        raise RuntimeError("no GPU visible to PyTorch")

    # A machine keeps the function loaded between calls, so what is stored
    # here is still in GPU memory for the next call that lands on it.
    if "model" not in _loaded:
        _loaded["tokenizer"] = AutoTokenizer.from_pretrained(MODEL)
        _loaded["model"] = AutoModelForSequenceClassification.from_pretrained(MODEL).to("cuda").eval()
    tokenizer, model = _loaded["tokenizer"], _loaded["model"]

    batch = tokenizer(texts, padding=True, truncation=True, return_tensors="pt").to("cuda")
    with torch.no_grad():
        probs = torch.softmax(model(**batch).logits, dim=-1)
    labels = [model.config.id2label[i] for i in probs.argmax(dim=-1).tolist()]
    return {
        "device": torch.cuda.get_device_name(0),
        "predictions": [
            {"text": t, "label": label, "score": round(float(p.max()), 4)}
            for t, label, p in zip(texts, labels, probs)
        ],
    }


if __name__ == "__main__":
    out = classify.remote(["I love this GPU.", "The queue was far too long."])
    print("Ran on:", out["device"])
    for p in out["predictions"]:
        print(f"  {p['label']:8} {p['score']:.4f}  {p['text']}")
