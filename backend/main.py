from fastapi import FastAPI

from telemetry_store import get_latest_telemetry

app = FastAPI()


@app.get("/")
def root():
    return {
        "status": "Connected Vehicle Telemetry Dashboard"
    }


@app.get("/telemetry")
def telemetry():
    return get_latest_telemetry()