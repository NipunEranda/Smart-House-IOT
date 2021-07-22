#MQTT Client

import paho.mqtt.client as mqtt

host = "5.196.95.208"
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("iotSmartHouse001/lightDecision")

def on_message(client, userdata, msg):
	value = str(msg.payload).replace("'", "").replace("b", "")
	print("")
	print("Value : " + value.split(",")[0])
	print("Decision : " + value.split(",")[1])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, 1883, 60)
client.loop_forever()
