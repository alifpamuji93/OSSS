import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)
 
try:
    while True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"
        else:
            print "Motion Detected!"
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
