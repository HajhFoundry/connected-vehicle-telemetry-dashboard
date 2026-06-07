import json
import threading

import paho.mqtt.client as mqtt

from backend.telemetry_store import update_telemetry

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "vehicle/telemetry"


def on_connect(client, userdata, flags, rc):
    print("FastAPI MQTT client connected")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    update_telemetry(payload)

    print("Telemetry received by FastAPI backend:")
    print(payload)


def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    mqtt_thread = threading.Thread(target=client.loop_forever)
    mqtt_thread.daemon = True
    mqtt_thread.start()