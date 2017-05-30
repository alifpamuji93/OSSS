import RPi.GPIO as GPIO
     
GPIO.setmode(GPIO.BCM)
relayPin = 17

def lampu_on():
    print ("Lampu menyala")

    GPIO.setwarnings(False)
    GPIO.setup(relayPin, GPIO.OUT)

def lampu_off():
    GPIO.cleanup(relayPin)
