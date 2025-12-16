import paho.mqtt.client as mqtt
import time
import json

device_id = "novautics_intercom_001"
topic = f"devices/{device_id}/events"

client = mqtt.Client(device_id)
client.connect("test.mosquitto.org", 1883, 60)

client.loop_start()

while True:
    payload = {
        "event": "doorbell_pressed",
        "device": device_id
    }
    client.publish(topic, json.dumps(payload))
    print("Doorbell ringing")
    time.sleep(5)
