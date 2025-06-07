#!/usr/bin/env bash
set -euo pipefail

MODEL="${DEFAULT_MODEL:-Llama-2-7b-chat-glm-4b-q0f16_0}"
echo "[INFO] Starting FastAPI server with model $MODEL on 0.0.0.0:${PORT:-8000} ..."
exec mlc_llm serve --model "$MODEL" --host 0.0.0.0 --port "${PORT:-8000}"
