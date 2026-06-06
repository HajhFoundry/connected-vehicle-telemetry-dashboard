import json

import paho.mqtt.client as mqtt
from telemetry_store import update_telemetry

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "vehicle/telemetry"

latest_telemetry = {}


def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    global latest_telemetry

    payload = json.loads(msg.payload.decode())

    latest_telemetry = payload
    update_telemetry(payload)

    print("\nTelemetry Received")
    print(payload)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

client.loop_forever()