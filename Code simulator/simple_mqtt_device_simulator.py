import paho.mqtt.client as mqtt
import time
import json

# ===== Device Identity =====
device_id = "novautics_intercom_001"

# ===== MQTT Broker (Azure VM) =====
mqtt_hub_hostname = "172.166.128.49"   # Replace with YOUR VM public IP
mqtt_hub_port = 22

# ===== MQTT Topic =====
topic = f"novautics/{device_id}/events"

# ===== MQTT Client =====
client = mqtt.Client(client_id=device_id)

# Connect to MQTT broker
client.connect(mqtt_hub_hostname, mqtt_hub_port, 60)
client.loop_start()

print("Connected to Novautics MQTT Broker")

# ===== Publish Events =====
try:
    while True:
        payload = {
            "device": device_id,
            "event": "doorbell_pressed",
            "timestamp": time.time()
        }

        client.publish(topic, json.dumps(payload))
        print("Doorbell event sent:", payload)
        time.sleep(5)

except KeyboardInterrupt:
    print("Simulator stopped")
    client.loop_stop()
    client.disconnect()

#############################results############################

Doorbell ringing 




