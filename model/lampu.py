import RPi.GPIO as GPIO
     
GPIO.setmode(GPIO.BCM)
relayPin = 17

def lampu_on():
    print ("Lampu menyala")

    GPIO.setwarnings(False)
    GPIO.setup(relayPin, GPIO.OUT)

def lampu_off():
    GPIO.cleanup(relayPin)


class Lampu(object):
	"""docstring for Lampu"""
	self.pin = 17

	def on(self):
		GPIO.setwarnings(False)
		return GPIO.setup(self.pin, GPIO.OUT)

	def off(self):
		return self GPIO.cleanup(self.pin)
		