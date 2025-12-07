# MQTT-HomeAssistant-HaripriyaP
Home Assistant MQTT publisher using Python for IoT assignment.

Home Assistant MQTT Integration – Assignment

Student Name: Haripriya P
Register Number: 42110441

1. Task Summary

I successfully configured Home Assistant + MQTT and created a Python script that publishes sensor values dynamically.
The data is subscribed inside Home Assistant using MQTT sensor and displayed in dashboard.

2. Tools Used

Home Assistant (VirtualBox)

Mosquitto MQTT Broker Add-on

Python (paho-mqtt library)

Visual Studio Code / File Editor Add-on


3. MQTT Topic Used
home/haripriyaP-2025/sensor



4. Python script

import paho.mqtt.client as mqtt
import time
import random

student_name = "Haripriya P"
unique_id = "42110441"
topic = "home/haripriyaP-2025/sensor"

broker = "192.168.56.101"
port = 1883
username = "mqttuser"
password = "Muruga@123"

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker, port, 60)

while True:
    value = random.randint(20, 40)
    msg = f"{student_name} - {unique_id} - {value}"
    client.publish(topic, msg)
    print("Published:", msg)
    time.sleep(2)

5. Home Assistant Configuration (configuration.yaml)
    mqtt:
       sensor:
    - name: "Haripriya MQTT Sensor"
      state_topic: "home/haripriyaP-2025/sensor"

6.Output / Result

MQTT messages published successfully from Python script

Message received in Home Assistant Developer Tools → MQTT

Sensor created and visible in Entities

Live data displayed on Dashboard card


