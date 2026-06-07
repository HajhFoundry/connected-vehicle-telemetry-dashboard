import json
import random
import time
from datetime import UTC, datetime

import paho.mqtt.client as mqtt

with open("config/simulator_config.json", "r") as file:
    config = json.load(file)

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "vehicle/telemetry"

vehicle_count = config["vehicle_count"]

VEHICLES = [
    f"VIN{10000+i}"
    for i in range(vehicle_count)
]


client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Connected to MQTT broker...")
print(f"Publishing to topic: {TOPIC}")

while True:
    for vehicle_id in VEHICLES:

        if config["low_battery_mode"]:
            battery_level = random.randint(5, 20)
        else:
            battery_level = random.randint(15, 100)

        if config["poor_signal_mode"]:
            signal_strength = random.randint(-110, -100)
        else:
            signal_strength = random.randint(-110, -60)

        if config["offline_mode"]:
            network_status = "DISCONNECTED"
        else:
            network_status = random.choice(
                ["CONNECTED", "CONNECTED", "CONNECTED", "DISCONNECTED"]
            )

        if config["ota_campaign_mode"]:
            ota_status = random.choice(
                ["DOWNLOADING", "INSTALLING"]
            )
        else:
            ota_status = random.choice(
                ["IDLE", "DOWNLOADING", "INSTALLING"]
            )

        telemetry = {
            "vehicle_id": vehicle_id,
            "timestamp": datetime.now(UTC).isoformat(),
            "speed": random.randint(0, 130),
            "battery_level": battery_level,
            "signal_strength": signal_strength,
            "network_status": network_status,
            "ota_status": ota_status,
        }

        payload = json.dumps(telemetry)
        client.publish(TOPIC, payload)

        print(payload)

    time.sleep(3)