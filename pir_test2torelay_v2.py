import RPi.GPIO as GPIO
import time
from lampu import lampu_on, lampu_off
from model.kirim import mail

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
            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
            time.sleep(3.0)
            lampu_on()
            time.sleep(10.0)
            
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
