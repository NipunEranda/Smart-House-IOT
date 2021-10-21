from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import request
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
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
led = {'led1': 11, 'led2': 13, 'led3': 15, 'led4': 12, 'led5': 16}
ledStatus = {
    'led1': 'off',
    'led2': 'off',
    'led3': 'off',
    'led4': 'off',
    'led5': 'off'
}
LED_LIST_ALL = ['led1', 'led2', 'led3', 'led4', 'led5']
LED_AUTO_LIST = []

GPIO.setwarnings(False)
GPIO.setup(led['led1'], GPIO.OUT)
GPIO.output(led['led1'], False)
GPIO.setup(led['led2'], GPIO.OUT)
GPIO.output(led['led2'], False)
GPIO.setup(led['led3'], GPIO.OUT)
GPIO.output(led['led3'], False)
GPIO.setup(led['led4'], GPIO.OUT)
GPIO.output(led['led4'], False)
GPIO.setup(led['led5'], GPIO.OUT)
GPIO.output(led['led5'], False)


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
            if (int(value) <= 200000):
                publish.single("iotSmartHouse001/lightDecision",
                               str(value) + ",OFF",
                               hostname=host)
                OFF_LED(LED_AUTO_LIST)
                output = str(value) + ",OFF"
            elif (int(value) > 200000):
                publish.single("iotSmartHouse001/lightDecision",
                               str(value) + ",ON",
                               hostname=host)
                ON_LED(LED_AUTO_LIST)
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
        ledStatus.update({x: 'on'})
        GPIO.output(led[x], True)


def OFF_LED(list):
    for x in list:
        ledStatus.update({x: 'off'})
        GPIO.output(led[x], False)


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


@app.route('/led/status', methods=['GET'], strict_slashes=False)
@cross_origin()
def getStatus():
    return ledStatus


@app.route('/led/auto/list', methods=['GET'], strict_slashes=False)
@cross_origin()
def getAutoList():
    return {'data': LED_AUTO_LIST}


@app.route('/led/on', methods=['GET'], strict_slashes=False)
@cross_origin()
def on():
    id = ''
    id = request.args.get('id')
    if (id is None):
        ON_LED(LED_LIST_ALL)
        return 'ALL LEDS ON'
    else:
        ON_LED([id])
        return (str(id) + ' ON')


@app.route('/led/off', methods=['GET'], strict_slashes=False)
@cross_origin()
def off():
    id = ''
    id = request.args.get('id')
    if (id is None):
        OFF_LED(LED_AUTO_LIST)
        LED_AUTO_LIST = []
        OFF_LED(LED_LIST_ALL)
        return 'ALL LEDS OFF'
    else:
        OFF_LED([id])
        return (str(id) + ' OFF')


@app.route('/led/auto', methods=['GET'], strict_slashes=False)
@cross_origin()
def setLedAuto():
    global LED_AUTO_LIST
    global LED_MANUAL_LIST
    output = ''
    id = request.args.get('id')
    status = request.args.get('status')
    if (id is None or status is None):
        LED_AUTO_LIST = []
        LED_MANUAL_LIST = []
        output = 'list cleared'
    else:
        if (status == 'on'):
            if (id not in LED_AUTO_LIST):
                LED_AUTO_LIST.append(id)
            output = 'led included'
        else:
            if (id in LED_AUTO_LIST):
                OFF_LED([id])
                LED_AUTO_LIST.remove(id)
            output = 'led excluded'
    return ('status : ' + output)


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
    try:
        initialDirCreator()
        th1 = threading.Thread(target=automate)

        th1.start()
        app.run(debug=True, host='0.0.0.0')

        th1.join()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
