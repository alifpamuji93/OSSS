import RPi.GPIO as GPIO
import time
from model.lampu import lampu_on, lampu_off
from model.kirim import mail
<<<<<<< HEAD:pir_test2torelay_v2.py
from model.kamera import rekam_on, rekam_off
=======
from model.camera import VideoCamera as camera

>>>>>>> refs/remotes/origin/master:app.py
GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)

 
try:
    while True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"
            rekam_off()
            
            lampu_off()
            
        else:
            print "Gerakan terdeteksi!"
            print "Kamera mulai merekam..."
<<<<<<< HEAD:pir_test2torelay_v2.py
            rekam_on()
=======
            camera.rekam()
>>>>>>> refs/remotes/origin/master:app.py
            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
            time.sleep(3.0)
            lampu_on()
            time.sleep(10.0)
            
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
