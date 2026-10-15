import pytest
from app.inference.engine import InferenceEngine
def test_inference():
    eng = InferenceEngine()
    res = eng.generate("Analyze Q3 earnings", "llama2-fin-7b-lora")
    assert res["tokens_per_sec"] > 50
