import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

# Default model used by the running server. This can be overridden by setting
# the ``DEFAULT_MODEL`` environment variable when starting the container.
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "Llama-2-7b-chat-glm-4b-q0f16_0")

app = FastAPI()
# Serve the simple WebLLM front-end under /demo
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/demo", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="demo")

@app.get("/")
def read_root():
    return {"message": "MLC-LLM server running"}


@app.get("/info")
def model_info():
    """Return information about the currently deployed model."""
    return {"default_model": DEFAULT_MODEL}

@app.post("/v1/chat/completions")
async def chat(request: Request):
    payload = await request.json()
    return {
        "model": payload.get("model"),
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Hello! I am a test model response."
                }
            }
        ]
    }
