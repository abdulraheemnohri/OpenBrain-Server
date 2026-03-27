from fastapi.testclient import TestClient
from backend.main import app
import json

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_v1_models():
    response = client.get("/v1/models")
    assert response.status_code == 200
    assert response.json()["object"] == "list"

def test_admin_api():
    # Create a key
    response = client.post("/api/admin/keys?usage_limit=100")
    assert response.status_code == 200
    key = response.json()["key"]
    assert key.startswith("sk-")

    # Get all keys
    response = client.get("/api/admin/keys")
    assert response.status_code == 200
    assert any(k["key"] == key for k in response.json())

    # Delete key
    response = client.delete(f"/api/admin/keys/{key}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get("/api/admin/keys")
    assert not any(k["key"] == key for k in response.json())

if __name__ == "__main__":
    # If run directly, maybe run some basic checks.
    print("Testing API endpoints via TestClient...")
    # These would normally be run by a test runner like pytest.
    # I'll include 'fastapi' and its dependencies in my manual test.
    test_root()
    test_v1_models()
    test_admin_api()
    print("Basic API tests passed!")
