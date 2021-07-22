#MQTT Publish

import paho.mqtt.publish as publish
while True:
	publish.single("coreElectronics/test", "Hello", hostname="test.mosquitto.org")
	publish.single("coreElectronics/topic", "world", hostname="test.mosquitto.org")
print("Done")
