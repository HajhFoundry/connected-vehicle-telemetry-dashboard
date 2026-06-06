import json
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "vehicle/telemetry"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Connected to MQTT broker...")
print(f"Publishing to topic: {TOPIC}")

while True:

    telemetry = {
        "vehicle_id": "VIN12345",
        "timestamp": datetime.utcnow().isoformat(),
        "speed": random.randint(0, 130),
        "battery_level": random.randint(20, 100),
        "signal_strength": random.randint(-110, -60),
        "network_status": random.choice(
            ["CONNECTED", "CONNECTED", "CONNECTED", "DISCONNECTED"]
        ),
        "ota_status": random.choice(
            ["IDLE", "DOWNLOADING", "INSTALLING"]
        )
    }

    payload = json.dumps(telemetry)

    client.publish(TOPIC, payload)

    print(payload)

    time.sleep(3)