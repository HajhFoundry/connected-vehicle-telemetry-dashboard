# MQTT Flow

## Topic

vehicle/telemetry

---

## Publisher

Vehicle Simulator

Publishes telemetry every 3 seconds.

Example:

{
  "vehicle_id": "VIN10000",
  "speed": 80,
  "battery_level": 65,
  "signal_strength": -75,
  "network_status": "CONNECTED",
  "ota_status": "IDLE"
}

---

## Broker

HiveMQ Public Broker

broker.hivemq.com

Port: 1883

---

## Subscriber

FastAPI MQTT Client

Receives telemetry.

Updates fleet telemetry store.

---

## Processing

Telemetry
    |
    v
Alert Engine
    |
    v
Health Engine
    |
    v
REST APIs
    |
    v
Dashboard

---

## Alerts

LOW_BATTERY

POOR_SIGNAL

VEHICLE_OFFLINE