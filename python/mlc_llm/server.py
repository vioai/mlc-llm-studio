import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

# Default model used by the running server. This can be overridden by setting
# the ``DEFAULT_MODEL`` environment variable when starting the container.
# DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "Llama-2-7b-chat-glm-4b-q0f16_0",)
DEFAULT_MODEL = "HF://mlc-ai/Phi-3.5-vision-instruct-q4f16_1-MLC"

app = FastAPI()
# Serve the simple WebLLM front-end under /demo
# The frontend lives in the repository root under ``frontend/``. When the
# package is installed in editable mode this directory sits two levels above
# this file (../../frontend).
REPO_FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"
PACKAGE_FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"
if PACKAGE_FRONTEND_DIR.exists():
    app.mount(
        "/demo",
        StaticFiles(directory=str(PACKAGE_FRONTEND_DIR), html=True),
        name="demo",
    )
elif REPO_FRONTEND_DIR.exists():
    app.mount(
        "/demo",
        StaticFiles(directory=str(REPO_FRONTEND_DIR), html=True),
        name="demo",
    )

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
