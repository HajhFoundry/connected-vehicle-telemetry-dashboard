from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"service_status": "UP"}


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "status" in response.json()


def test_alerts_endpoint():
    response = client.get("/alerts")

    assert response.status_code == 200
    assert "alerts" in response.json()


def test_vehicle_health_endpoint():
    response = client.get("/vehicle-health")

    assert response.status_code == 200
    assert "vehicle_status" in response.json()
    assert "health_score" in response.json()
    assert "alerts" in response.json()


def test_fleet_endpoint():
    response = client.get("/fleet")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)