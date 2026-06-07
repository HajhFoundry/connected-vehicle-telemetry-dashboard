import time

import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Connected Vehicle Telemetry Dashboard",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 Connected Vehicle Telemetry Dashboard")
st.caption("Real-time MQTT vehicle telemetry, health monitoring, and alert visualization")


def get_api_data(endpoint):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


telemetry = get_api_data("/telemetry")
vehicle_health = get_api_data("/vehicle-health")
alerts_response = get_api_data("/alerts")
service_health = get_api_data("/health")

if service_health:
    st.success("Backend Service: UP")
else:
    st.error("Backend Service: DOWN")

if not telemetry:
    st.warning("No telemetry received yet. Start the vehicle simulator and FastAPI backend.")
else:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Vehicle ID", telemetry.get("vehicle_id", "N/A"))
    col2.metric("Speed", f"{telemetry.get('speed', 0)} km/h")
    col3.metric("Battery", f"{telemetry.get('battery_level', 0)}%")
    col4.metric("Signal", f"{telemetry.get('signal_strength', 0)} dBm")

    st.divider()

    col5, col6, col7 = st.columns(3)

    col5.metric("Network Status", telemetry.get("network_status", "N/A"))
    col6.metric("OTA Status", telemetry.get("ota_status", "N/A"))

    if vehicle_health:
        col7.metric("Health Score", vehicle_health.get("health_score", 0))

    st.divider()

    st.subheader("Vehicle Health")

    if vehicle_health:
        status = vehicle_health.get("vehicle_status", "UNKNOWN")

        if status == "GOOD":
            st.success(f"Vehicle Status: {status}")
        elif status == "WARNING":
            st.warning(f"Vehicle Status: {status}")
        elif status == "CRITICAL":
            st.error(f"Vehicle Status: {status}")
        else:
            st.info(f"Vehicle Status: {status}")

    st.subheader("Active Alerts")

    alerts = []

    if alerts_response:
        alerts = alerts_response.get("alerts", [])

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("No active alerts")

    st.divider()

    st.subheader("Raw Telemetry Payload")
    st.json(telemetry)

time.sleep(3)
st.rerun()