import time

import pandas as pd
import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Connected Vehicle Fleet Dashboard",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 Connected Vehicle Fleet Telemetry Dashboard")
st.caption("Real-time MQTT fleet telemetry, vehicle health monitoring, and alert visualization")


def get_api_data(endpoint):
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=3)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


fleet_data = get_api_data("/fleet")
service_health = get_api_data("/health")

if service_health:
    st.success("Backend Service: UP")
else:
    st.error("Backend Service: DOWN")

if not fleet_data:
    st.warning("No fleet telemetry received yet. Start FastAPI and the vehicle simulator.")
else:
    vehicles = list(fleet_data.values())
    df = pd.DataFrame(vehicles)

    fleet_size = len(df)
    online_count = len(df[df["network_status"] == "CONNECTED"])
    offline_count = len(df[df["network_status"] == "DISCONNECTED"])
    low_battery_count = len(df[df["battery_level"] < 25])
    poor_signal_count = len(df[df["signal_strength"] < -100])

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Fleet Size", fleet_size)
    col2.metric("Online", online_count)
    col3.metric("Offline", offline_count)
    col4.metric("Low Battery", low_battery_count)
    col5.metric("Poor Signal", poor_signal_count)

    st.divider()

    st.subheader("Fleet Telemetry Table")
    st.dataframe(
        df[
            [
                "vehicle_id",
                "speed",
                "battery_level",
                "signal_strength",
                "network_status",
                "ota_status",
                "timestamp",
            ]
        ],
        use_container_width=True,
    )

    st.divider()

    st.subheader("Vehicles Requiring Attention")

    attention_df = df[
        (df["network_status"] == "DISCONNECTED")
        | (df["battery_level"] < 25)
        | (df["signal_strength"] < -100)
    ]

    if attention_df.empty:
        st.success("No vehicles currently require attention.")
    else:
        st.warning(f"{len(attention_df)} vehicle(s) require attention.")
        st.dataframe(attention_df, use_container_width=True)

    st.divider()

    st.subheader("Raw Fleet Payload")
    st.json(fleet_data)

time.sleep(3)
st.rerun()