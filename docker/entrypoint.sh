#!/usr/bin/env bash
set -euo pipefail

if [[ $# -gt 0 ]]; then
  # If arguments are provided, execute them instead of starting the server.
  exec "$@"
else
  MODEL="${DEFAULT_MODEL:-phi-3-mini-4k-instruct-q4f16_1}"
  echo "[INFO] Starting FastAPI server with model $MODEL on 0.0.0.0:${PORT:-8000}..."
  exec mlc_llm serve --model "$MODEL" --host 0.0.0.0 --port "${PORT:-8000}"
fi

