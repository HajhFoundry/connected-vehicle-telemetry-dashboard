from fastapi import FastAPI

from backend.telemetry_store import get_latest_telemetry
from backend.alert_engine import generate_alerts, calculate_health_score
from backend.mqtt_client import start_mqtt_client

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_mqtt_client()

@app.get("/")
def root():
    return {"status": "Connected Vehicle Telemetry Dashboard"}


@app.get("/health")
def health():
    return {"service_status": "UP"}


@app.get("/telemetry")
def telemetry():
    return get_latest_telemetry()


@app.get("/alerts")
def alerts():
    telemetry_data = get_latest_telemetry()
    return {"alerts": generate_alerts(telemetry_data)}


@app.get("/vehicle-health")
def vehicle_health():
    telemetry_data = get_latest_telemetry()

    if not telemetry_data:
        return {
            "vehicle_status": "NO_DATA",
            "health_score": 0,
            "alerts": [],
        }

    alerts_list = generate_alerts(telemetry_data)
    health_score = calculate_health_score(telemetry_data)

    vehicle_status = "GOOD"

    if health_score < 70:
        vehicle_status = "WARNING"

    if health_score < 40:
        vehicle_status = "CRITICAL"

    return {
        "vehicle_status": vehicle_status,
        "health_score": health_score,
        "alerts": alerts_list,
    }