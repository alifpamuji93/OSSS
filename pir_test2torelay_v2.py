import RPi.GPIO as GPIO
import time
from lampu import lampu_on, lampu_off

GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)

 
try:
    while True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"

            lampu_off()
            
        else:
            print "Gerakan terdeteksi!"
            print "Kamera mulai merekam..."

            time.sleep(3.0)
            lampu_on()
            time.sleep(10.0)
            
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
