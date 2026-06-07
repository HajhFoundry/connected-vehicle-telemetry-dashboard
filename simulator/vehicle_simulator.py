import json
import random
import time
from datetime import UTC, datetime

import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "vehicle/telemetry"

VEHICLES = [
    "VIN12345",
    "VIN23456",
    "VIN34567",
    "VIN45678",
    "VIN56789",
]

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Connected to MQTT broker...")
print(f"Publishing to topic: {TOPIC}")

while True:
    for vehicle_id in VEHICLES:
        telemetry = {
            "vehicle_id": vehicle_id,
            "timestamp": datetime.now(UTC).isoformat(),
            "speed": random.randint(0, 130),
            "battery_level": random.randint(15, 100),
            "signal_strength": random.randint(-110, -60),
            "network_status": random.choice(
                ["CONNECTED", "CONNECTED", "CONNECTED", "DISCONNECTED"]
            ),
            "ota_status": random.choice(
                ["IDLE", "DOWNLOADING", "INSTALLING"]
            ),
        }

        payload = json.dumps(telemetry)
        client.publish(TOPIC, payload)

        print(payload)

    time.sleep(3)