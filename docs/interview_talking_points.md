# Interview Talking Points

## Project Summary

I built a Connected Vehicle Fleet Telemetry Platform to simulate vehicle-to-cloud communication.

The platform uses MQTT to publish telemetry from multiple simulated vehicles, FastAPI to process telemetry and expose APIs, and Streamlit to provide a fleet monitoring dashboard.

---

## Business Problem

Connected vehicle teams need visibility into fleet health, connectivity, OTA status, and vehicle telemetry.

This platform demonstrates how telemetry can be collected, analyzed, and visualized.

---

## Architecture

Vehicle Simulator

→ MQTT Broker

→ FastAPI Backend

→ Alert Engine

→ Health Engine

→ Dashboard

---

## Features

- Multi-Vehicle Fleet Simulation
- MQTT Communication
- Vehicle Health Scoring
- Alert Generation
- Fleet Monitoring Dashboard
- Automated Testing
- GitHub Actions CI/CD
- Configurable Simulation Scenarios

---

## Challenges Solved

- MQTT message handling
- Fleet telemetry aggregation
- Health score calculation
- Alert generation
- Automated validation through Pytest
- CI/CD integration

---

## Technologies

- Python
- MQTT
- FastAPI
- Streamlit
- Pytest
- GitHub Actions

---

## Results

Created a fully functional fleet telemetry platform that simulates connected vehicle behavior and demonstrates telematics monitoring concepts commonly used in automotive OEM environments.