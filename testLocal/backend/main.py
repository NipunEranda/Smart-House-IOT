from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from random import randint
import csv
import os
import threading

host = "5.196.95.208"
automationStatus = True
value = ""
output = ""


def automate():
    while True:
        global automationStatus
        global value
        global output
        
        value = str(randint(0, 20))
        
        if (int(value) <= 10):
            output = str(value) + ",OFF"
        elif (int(value) > 10):
            output = str(value) + ",ON"


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


@app.route('/led/on', methods=['GET'], strict_slashes=False)
@cross_origin()
def on():
    #GPIO.output(led, True)
    return 'LED ON'


@app.route('/led/off', methods=['GET'], strict_slashes=False)
@cross_origin()
def off():
    #GPIO.output(led, False)
    return 'LED OFF'


@app.route('/mod/manual', methods=['GET'], strict_slashes=False)
@cross_origin()
def manual():
    global automationStatus
    automationStatus = False
    return str("Status : " + str(automationStatus))
    #return 'MANUAL CONTROL ENABLED'


@app.route('/mod/auto', methods=['GET'], strict_slashes=False)
@cross_origin()
def auto():
    global automationStatus
    automationStatus = True
    return str("Status : " + str(automationStatus))
    #return 'AUTOMATION ENABLED'


@app.route('/data/current', methods=['GET'], strict_slashes=False)
@cross_origin()
def getData():
    return output


#return str(rc_time(ldr))

if __name__ == '__main__':
    initialDirCreator()
    th1 = threading.Thread(target=automate)
    th2 = threading.Thread(target=app.run)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    #app.run(debug=True, host='0.0.0.0')
