#MQTT Client
from time import sleep
import paho.mqtt.client as mqtt
import os

host = "test.mosquitto.org"
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("iotSmartHouse001/ldr/mod")

def on_message(client, userdata, msg):
	value = str(msg.payload).replace("'", "").replace("b", "")
	os.remove("mod")
	f = open("mod", "w")
	f.write(value)
	f.close()
	sleep(1000)
	print(value)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, 1883, 60)
client.loop_forever()