from typing import Dict
class InferenceEngine:
    def generate(self, prompt: str, model: str) -> Dict:
        return {"model": model, "answer": f"[vLLM] Financial analysis for {prompt[:50]}...", "tokens_per_sec": 145}
