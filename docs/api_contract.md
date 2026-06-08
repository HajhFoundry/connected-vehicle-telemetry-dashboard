# API Contract

Base URL

```text
http://127.0.0.1:8000
```

---

## GET /

Returns platform status.

Response

```json
{
  "status": "Connected Vehicle Telemetry Dashboard"
}
```

---

## GET /health

Response

```json
{
  "service_status": "UP"
}
```

---

## GET /telemetry

Returns latest telemetry.

---

## GET /fleet

Returns telemetry for all vehicles.

---

## GET /alerts

Response

```json
{
  "alerts": [
    "LOW_BATTERY"
  ]
}
```

---

## GET /vehicle-health

Response

```json
{
  "vehicle_status": "GOOD",
  "health_score": 100,
  "alerts": []
}
```