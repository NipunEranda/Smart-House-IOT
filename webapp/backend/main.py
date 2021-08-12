from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
delayT = .1
value = 0 #LDR Value
ldr = 7 # LDR pin number
led = 11 # LED Pin number

GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

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
        return 'MANUAL CONTROL ENABLED'

@app.route('/mod/auto', methods=['GET'], strict_slashes=False)
@cross_origin()
def auto():
        return 'AUTOMATION ENABLED'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
