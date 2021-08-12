import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
delayT = .1
value = 0 #LDR Value
ldr = 7 # LDR pin number
led = 11 # LED Pin number

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

def rc_time(ldr):
        count = 0

        GPIO.setup(ldr, GPIO.OUT)
        GPIO.output(ldr, False)
        time.sleep(delayT)

        GPIO.setup(ldr, GPIO.IN)

        while(GPIO.input(ldr) == 0):
                count += 1

        return count

try:
        while True:
                value = rc_time(ldr)
		print(value)

        	if(int(value) <= 100000):
                	print("Lights are OFF")
                	GPIO.output(led, False)
        	if(int(value) > 100000):
                	print("Lights are ON")
                	GPIO.output(led, True)

except KeyboardInterrupt:
        pass
finally:
        GPIO.cleanup()
