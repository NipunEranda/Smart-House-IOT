#MQTT Publish
from random import randint

import paho.mqtt.publish as publish

host = "5.196.95.208"
while True:
	x = randint(0, 2000)
	if(x > 0 and x < 500):
		publish.single("iotSmartHouse001/lightDecision", str(x) + ",Low", hostname=host)
	elif(x > 500 and x < 1000):
		publish.single("iotSmartHouse001/lightDecision", str(x) + ",Medium", hostname=host)
	elif(x > 1000):
		publish.single("iotSmartHouse001/lightDecision", str(x) + ",High", hostname=host)
	else:
		publish.single("iotSmartHouse001/lightDecision", "Error", hostname=host)
	