import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_RELAY = 27
GPIO_TRIGGER = 23
GPIO_ECHO = 22
dist = 2

GPIO.setup(GPIO_RELAY, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

#print 'Testing motor on. CTRL C to quit'
#GPIO.output(GPIO_RELAY, GPIO.LOW)
#time.sleep(2)
#print 'Testing motor off. CTRL C to quit'
#GPIO.output(GPIO_RELAY, GPIO.HIGH)
#time.sleep(2)


if __name__ == '__main__':
	GPIO.output(GPIO_RELAY, GPIO.LOW)
	try:
		while dist <= 11:
	        	dist = distance()
			print ("Measured Distance = %.1f cm" % dist)
			
			time.sleep(1)
		else:
			GPIO.output(GPIO_RELAY, GPIO.HIGH)
			GPIO.cleanup()


	except KeyboardInterrupt:
        	print("Measurement stopped by User")
		GPIO.output(GPIO_RELAY, GPIO.HIGH)
	        GPIO.cleanup()
