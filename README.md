# MLC-LLM Studio

MLC-LLM Studio provides a fully automated pipeline to build, test and deploy the [MLC-LLM](https://llm.mlc.ai/) framework. The repository supplies a multipurpose Docker image for local development and CI builds, along with a GitHub Actions workflow that packages cross‑platform wheels and publishes them as GitHub releases.

---

## Features

- **Multipurpose Docker Image** – single image for development or production, published to GHCR.
- **Automated Tests** ensure the image works as expected.
- **CI/CD Pipeline** builds wheels for Linux and Windows and creates releases.

For detailed documentation see [docs/README.md](docs/README.md) and [docs/ci.md](docs/ci.md).

---

## Project Structure

```text
.
├── docker/                 # Dockerfile and helper scripts
├── docs/                   # Additional documentation and diagrams
├── python/                 # Source code of the mlc_llm Python package
├── scripts/                # Test and startup scripts
└── .github/workflows/      # CI configuration
```

---

## Architecture Diagrams

### Build & Deployment Flow

![Build & Deployment Flow](docs/assets/CI_CD%20Pipeline%20for%20Docker%20Deployment.png)

### CI/CD Architecture

![CI/CD Architecture](docs/assets/MLC-LLM%20CI_CD%20Architecture%20Flowchart.png)

### Model Deployment

![Model Deployment](docs/assets/Model%20Deployment%20Process.png)

---

## CI/CD Flow Summary

```mermaid
graph TD
  A[Push or Tag to GitHub] --> B[Build & Push Docker Image]
  B --> C[Run Tests in Container]
  C --> D[Build Wheels on Linux/Windows]
  D --> E[Create GitHub Release]
```

---

## Local Development

```bash
# Build the Docker image
docker build -t mlc-llm-dev -f docker/Dockerfile .

# Start an interactive shell with the repo mounted
docker run --rm -it -v "$PWD:/workspace" mlc-llm-dev bash

# (inside container) install the package and run tests
pip install -e python
pytest python/tests
```

## Live Demo & Sample Output

The CI/CD pipeline deploys the Docker image to **Fly.io**. A **demo** server is
running at <https://mlc-llm.fly.dev/> using the quantized model
`phi-3-mini-4k-instruct-q4f16_1`.

> **Note**
> This server is intended purely for demonstration. It runs with CPU only
> because GitHub Actions does not provide GPU runners. The underlying
> [MLC-LLM](https://llm.mlc.ai/) framework supports serving models on CPUs,
> GPUs and other accelerators.

To use a different model, set a `DEFAULT_MODEL` environment variable (or edit
`fly.toml`) and ensure `docker/entrypoint.sh` reads this value as shown in
[docs/ci.md](docs/ci.md#5-replacing-models).
**Tip**: For quick local tests, you can download the smaller quantized model `Llama-2-7b-chat-hf-q4f16_1` and serve it as shown in [docs/README.md](docs/README.md#local-development-instructions).


The currently deployed model can be verified by querying the `/info` endpoint:

```bash
curl https://mlc-llm.fly.dev/info
# {"default_model":"phi-3-mini-4k-instruct-q4f16_1"}
```

```bash
curl https://mlc-llm.fly.dev/
# {"message":"MLC-LLM server running"}

curl -X POST https://mlc-llm.fly.dev/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "phi-3-mini-4k-instruct-q4f16_1",
        "messages": [
          {"role": "user", "content": "Hello, who are you?"}
        ]
      }'
# {"model":"phi-3-mini-4k-instruct-q4f16_1","choices":[{"message":{"role":"assistant","content":"Hello! I am a test model response."}}]}
```

A minimal WebLLM front-end is served from the container under `/demo`. Visit
`https://mlc-llm.fly.dev/demo` to try a browser-based chat interface.

## Future Work

- Add optional Swagger UI (`/docs`) for interactive exploration.
- Deploy on GPU-backed nodes (AWS EC2/GCP) for realistic speed tests.
- Improve configuration options for deploying various models.

---

Maintained by the MLC-LLM Studio contributors.

