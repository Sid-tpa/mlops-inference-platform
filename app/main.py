from fastapi import FastAPI
from app.inference.engine import InferenceEngine
app = FastAPI(title="MLOps Inference Platform - vLLM + Fine-tuning")
engine = InferenceEngine()
@app.get("/health")
def health(): return {"vllm": "ready", "mlflow": "connected", "models": ["llama2-fin-7b-lora"]}
@app.post("/api/v1/inference/generate")
def generate(prompt: str, model: str = "llama2-fin-7b-lora"): return engine.generate(prompt, model)
