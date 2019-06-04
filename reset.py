import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO =  27
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

GPIO.cleanup()
