#MQTT Publish
from random import randint
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
delayT = .1
value = 0 #LDR Value
mod = 'auto'
ldr = 7 # LDR pin number

host = "5.196.95.208"

def publishMod():
        f = open("mod", "r")
        mod = f.read()
        f.close()
        publish.single("iotSmartHouse001/ldr/mod/current", str(mod), hostname=host)

def rc_time(ldr):
        count = 0

        GPIO.setup(ldr, GPIO.OUT)
        GPIO.output(ldr, False)
        time.sleep(delayT)

        GPIO.setup(ldr, GPIO.IN)

        while(GPIO.input(ldr) == 0):
                count += 1

        return count

print("Server Started.")
try:
        while True:
                value = rc_time(ldr)
                publishMod()
                if(int(value) <= 400000):
                        publish.single("iotSmartHouse001/lightDecision", str(value) + ",OFF", hostname=host)
                if(int(value) > 400000):
                        publish.single("iotSmartHouse001/lightDecision", str(value) + ",ON", hostname=host)

except KeyboardInterrupt:
        pass
finally:
        GPIO.cleanup()
