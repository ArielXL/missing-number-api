from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_missing_ok():
    r = client.post("/api/missing", json={"number": 57})
    assert r.status_code == 200
    data = r.json()
    assert data["extracted"] == 57
    assert data["missing"] == 57


def test_missing_invalid_low():
    r = client.post("/api/missing", json={"number": 0})
    assert r.status_code == 422


def test_missing_invalid_high():
    r = client.post("/api/missing", json={"number": 101})
    assert r.status_code == 422
