import pytest

try:
    from fastapi.testclient import TestClient
except Exception:  # pragma: no cover - optional dependency
    pytest.skip("fastapi TestClient dependencies missing", allow_module_level=True)

from mlc_llm.server import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "MLC-LLM server running"}

def test_chat_endpoint():
    payload = {"model": "test", "messages": [{"role": "user", "content": "Hi"}]}
    response = client.post("/v1/chat/completions", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("model") == "test"
    assert body["choices"][0]["message"]["role"] == "assistant"
    assert "test model response" in body["choices"][0]["message"]["content"]


def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    body = response.json()
    assert "default_model" in body
