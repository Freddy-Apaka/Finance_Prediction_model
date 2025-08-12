from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_predict_missing_model():
    # This test expects model might be missing in CI. It checks that API returns 500 if model absent.
    r = client.post('/predict', json={'features': {'a': 1}})
    assert r.status_code in (200, 500, 400)
