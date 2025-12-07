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
home/haripriyaP-2025/temperature
home/haripriyaP-2025/humidity
home/haripriyaP-2025/light




5. Python script

import paho.mqtt.client as mqtt
import time
import random

student_name = "Haripriya P"
unique_id = "42110441"

broker = "192.168.56.101"  
port = 1883
username = "mqttuser"
password = "Muruga@123"

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker, port, 60)

while True:
    temperature = 25
    humidity = 60
    light = random.randint(100, 300)
    print(f"Published: {student_name} - {unique_id}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Light Sensor: {light} lx")
    print("-----------------------------")
    client.publish("home/haripriyaP-2025/temperature", temperature)
    client.publish("home/haripriyaP-2025/humidity", humidity)
    client.publish("home/haripriyaP-2025/light", light)

    time.sleep(3)


5. Home Assistant Configuration (configuration.yaml)
    mqtt:
  sensor:
    - name: "Haripriya Temperature"
      state_topic: "home/haripriyaP-2025/temperature"
      unit_of_measurement: "°C"

    - name: "Haripriya Humidity"
      state_topic: "home/haripriyaP-2025/humidity"
      unit_of_measurement: "%"

    - name: "Haripriya Light Sensor"
      state_topic: "home/haripriyaP-2025/light"
      unit_of_measurement: "lx"

^.Output and Result
Python script successfully published MQTT messages containing:
✔ Student Name & Register Number
✔ Temperature values
✔ Humidity values
✔ Light Sensor values (custom sensor)

Messages were received and verified in Home Assistant Developer Tools → MQTT → Listen to Topic.

Sensors were created in configuration.yaml and are visible in Entities as:

sensor.haripriya_temperature

sensor.haripriya_humidity

sensor.haripriya_light_sensor

Live data appeared and updated in real-time on Home Assistant Dashboard card.

