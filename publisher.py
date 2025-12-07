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
