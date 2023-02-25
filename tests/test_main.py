from fastapi.testclient import TestClient

from app.main import api_service

client = TestClient(api_service)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
