import RPi.GPIO as GPIO
     
GPIO.setmode(GPIO.BCM)
relayPin = 17
pirPin = 18

GPIO.setwarnings(False)
GPIO.setup(pirPin, GPIO.IN)

while True:
	if GPIO.input(pirPin) == GPIO.HIGH:
		GPIO.setup(relayPin, GPIO.OUT)
		print "motion detected"

	else:
		GPIO.cleanup(relayPin)
		print "no motion"