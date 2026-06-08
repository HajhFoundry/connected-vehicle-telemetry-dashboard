# Connected Vehicle Fleet Telemetry Platform

## Overview

This project simulates a connected vehicle fleet that publishes telemetry data through MQTT.

The platform consumes telemetry, analyzes vehicle health, generates alerts, exposes APIs through FastAPI, and visualizes fleet status through Streamlit.

---

## Architecture

Vehicle Simulator
        |
        v
MQTT Broker (HiveMQ)
        |
        v
MQTT Subscriber (FastAPI Backend)
        |
        +-------------------+
        |                   |
        v                   v
Telemetry Store      Alert Engine
        |                   |
        +---------+---------+
                  |
                  v
          Vehicle Health Engine
                  |
                  v
              FastAPI APIs
                  |
                  v
          Streamlit Dashboard

---

## Components

### Vehicle Simulator

Generates simulated vehicle telemetry.

Metrics:

- Vehicle ID
- Speed
- Battery Level
- Signal Strength
- Network Status
- OTA Status

---

### MQTT Broker

Receives telemetry messages from vehicles.

Protocol:

MQTT

Topic:

vehicle/telemetry

---

### FastAPI Backend

Processes telemetry.

Responsibilities:

- Receive MQTT messages
- Store latest telemetry
- Generate alerts
- Calculate health score
- Expose REST APIs

---

### Streamlit Dashboard

Provides fleet monitoring view.

Features:

- Fleet Size
- Online Vehicles
- Offline Vehicles
- Low Battery Vehicles
- Poor Signal Vehicles
- Fleet Table
- Attention Queue

---

## Technology Stack

- Python
- MQTT
- HiveMQ
- FastAPI
- Streamlit
- Pytest
- GitHub Actions