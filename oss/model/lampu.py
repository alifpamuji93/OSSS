import RPi.GPIO as GPIO
     
GPIO.setmode(GPIO.BCM)
relayPin = 17
GPIO.setwarnings(False)

def lampu_on():
    print ("Lampu menyala")

    GPIO.setwarnings(False)
    GPIO.setup(relayPin, GPIO.OUT)

def lampu_off():
    GPIO.cleanup(relayPin)


class relay(object):
    def __init__():
        self.relayPin = 17

    def on(self):
        return GPIO.setup(self.relayPin, GPIO.OUT)

    def off(self):
        return GPIO.cleanup(self.relayPin)
