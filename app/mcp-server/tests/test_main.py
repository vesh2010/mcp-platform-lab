from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["application"] == "mcp-platform"


def test_tools():
    response = client.get("/tools")
    assert response.status_code == 200
    assert response.json()["tools"][0]["name"] == "get_platform_info"
