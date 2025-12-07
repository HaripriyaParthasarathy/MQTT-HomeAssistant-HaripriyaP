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
