#MQTT Publish
from random import randint
import paho.mqtt.publish as publish

host = "test.mosquitto.org"

print("Server Started.")
while True:
	x = randint(0, 2000)
	if(x > 0 and x < 500):
		publish.single("iotSmartHouse001/lightDecision", str(x), hostname=host)
	elif(x > 500 and x < 1000):
		publish.single("iotSmartHouse001/lightDecision", str(x), hostname=host)
	elif(x > 1000):
		publish.single("iotSmartHouse001/lightDecision", str(x), hostname=host)
	else:
		publish.single("iotSmartHouse001/lightDecision", "0", hostname=host)
	
