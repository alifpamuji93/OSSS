import RPi.GPIO as GPIO
import cv2
import time
from model.lampu import lampu_on, lampu_off
from model.kirim import mail
from model.camera import VideoCamera as camera

GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)

 
try:
    while True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"
##            rekam_off()
            
            lampu_off()
            
        else:
            print "Gerakan terdeteksi!"
            print "Kamera mulai merekam..."

##            camera.rekam()

            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
            time.sleep(3.0)
            lampu_on()
            time.sleep(10.0)
            
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
