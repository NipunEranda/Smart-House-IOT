from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time
import csv
import os
import threading

host = "5.196.95.208"
automationStatus = False
value = ""
output = ""
LED_ON_LIST = []
LED_OFF_LIST = []

GPIO.setmode(GPIO.BOARD)
delayT = .1
value = 0  #LDR Value
ldr = 7  # LDR pin number
led1 = 11  # LED1 Pin number
led2 = 13 #LED2 Pin number
led3 = 15 #LED3 Pin number
led4 = 12  #LED4 Pin number

GPIO.setwarnings(False)
GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, False)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, False)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led3, False)
GPIO.setup(led4, GPIO.OUT)
GPIO.output(led4, False)

def rc_time(ldr):
    count = 0

    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayT)

    GPIO.setup(ldr, GPIO.IN)

    while (GPIO.input(ldr) == 0):
        count += 1

    return count


def automate():
    while True:
        global automationStatus
        global value
        global output
	global LED_ON_LIST
	global LED_OFF_LIST
        if (automationStatus == True):
            value = rc_time(ldr)
            if (int(value) <= 100000):
                publish.single("iotSmartHouse001/lightDecision",
                               str(value) + ",OFF",
                               hostname=host)
                GPIO.output(led, False)
                output = str(value) + ",OFF"
            
            elif (int(value) > 100000):
                publish.single("iotSmartHouse001/lightDecision",
                           str(value) + ",ON",
                           hostname=host)
                GPIO.output(led, True)
                output = str(value) + ",ON"
        else:
            value = str(0)


def initialDirCreator():
    homedir = os.environ['HOME']
    if (os.path.isfile(homedir + "/scheduler.csv")):
        f = open(homedir + '/scheduler.csv', 'r')
        reader = csv.reader(f)
        lineCount = len(list(reader))
        if (lineCount < 1):
            f = open(homedir + '/scheduler.csv', 'w')
            writer = csv.writer(f)
            writer.writerow('id', 'day', 'time', 'status')
            f.close()
    else:
        f = open(homedir + '/scheduler.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['id', 'day', 'time', 'status'])
        f.close()

def ON_LED(list):
	for x in list:
		GPIO.output(x, True)

def OFF_LED(list):
	for x in list:
		GPIO.output(x, False)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

@app.route('/led/on', methods=['GET'], strict_slashes=False)
@cross_origin()
def on():
    ON_LED([led1, led2, led3, led4])
    return 'ALL LEDS ON'

@app.route('/led/on/led1', methods=['GET'], strict_slashes=False)
@cross_origin()
def on1():
    ON_LED([led1])
    return 'LED 1 ON'

@app.route('/led/on/led2', methods=['GET'], strict_slashes=False)
@cross_origin()
def on2():
    ON_LED([led2])
    return 'LED 2 ON'

@app.route('/led/on/led3', methods=['GET'], strict_slashes=False)
@cross_origin()
def on3():
    ON_LED([led3])
    return 'LED 3 ON'

@app.route('/led/on/led4', methods=['GET'], strict_slashes=False)
@cross_origin()
def on4():
    ON_LED([led4])
    return 'LED 4 ON'

@app.route('/led/off', methods=['GET'], strict_slashes=False)
@cross_origin()
def off():
    OFF_LED([led1, led2, led3, led4])
    return 'ALL LEDS OFF'

@app.route('/led/off/led1', methods=['GET'], strict_slashes=False)
@cross_origin()
def off1():
    OFF_LED([led1])
    return 'LED 1 OFF'

@app.route('/led/off/led2', methods=['GET'], strict_slashes=False)
@cross_origin()
def off2():
    OFF_LED([led2])
    return 'LED 2 OFF'

@app.route('/led/off/led3', methods=['GET'], strict_slashes=False)
@cross_origin()
def off3():
    OFF_LED([led3])
    return 'LED 3 OFF'

@app.route('/led/off/led4', methods=['GET'], strict_slashes=False)
@cross_origin()
def off4():
    OFF_LED([led4])
    return 'LED 4 OFF'

@app.route('/mod/manual', methods=['GET'], strict_slashes=False)
@cross_origin()
def manual():
    global automationStatus
    automationStatus = False
    return 'manual'


@app.route('/mod/auto', methods=['GET'], strict_slashes=False)
@cross_origin()
def auto():
    global automationStatus
    automationStatus = True
    return 'auto'


@app.route('/data/current', methods=['GET'], strict_slashes=False)
@cross_origin()
def getData():
    global output
    return output

if __name__ == '__main__':
    initialDirCreator()
#    th1 = threading.Thread(target=automate)
    #th2 = threading.Thread(target=appRun)

#    th1.start()
    app.run(debug=True, host='0.0.0.0')

#    th1.join()
