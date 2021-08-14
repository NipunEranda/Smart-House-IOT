from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import csv
import os
import threading

host = "5.196.95.208"
automationStatus = True
value = ""
output = ""

GPIO.setmode(GPIO.BOARD)
delayT = .1
value = 0  #LDR Value
ldr = 7  # LDR pin number
led = 11  # LED Pin number

GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)


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
        if (automationStatus == True):
            value = rc_time(ldr)
            if (int(value) <= 100000):
                print("Lights are OFF")
                publish.single("iotSmartHouse001/lightDecision",
                               str(value) + ",OFF",
                               hostname=host)
                GPIO.output(led, False)
                output = str(value) + ",OFF"
            
            elif (int(value) > 100000):
                print("Lights are ON")
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


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

initialDirCreator()

th = threading.Thread(target=automate)
th.start()
th.join()


@app.route('/led/on', methods=['GET'], strict_slashes=False)
@cross_origin()
def on():
    GPIO.output(led, True)
    return 'LED ON'


@app.route('/led/off', methods=['GET'], strict_slashes=False)
@cross_origin()
def off():
    GPIO.output(led, False)
    return 'LED OFF'


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
    th1 = threading.Thread(target=automate)
    th2 = threading.Thread(target=app.run)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    #app.run(debug=True, host='0.0.0.0')
