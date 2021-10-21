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
led = 11 # LED Pin number

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

host = "5.196.95.208"

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
                f = open("mod", "r")
                mod = f.read()
                f.close()
                publish.single("iotSmartHouse001/ldr/mod", str(mod), hostname=host)
                if(int(value) <= 100000):
#                        print("Lights are OFF")
                        publish.single("iotSmartHouse001/lightDecision", str(value) + ",OFF", hostname=host)
                        GPIO.output(led, False)
                if(int(value) > 100000):
#                        print("Lights are ON")
                        publish.single("iotSmartHouse001/lightDecision", str(value) + ",ON", hostname=host)
                        GPIO.output(led, True)

except KeyboardInterrupt:
        pass
finally:
        GPIO.cleanup()
