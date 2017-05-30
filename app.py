
import RPi.GPIO as GPIO
import cv2
import time
from datetime import datetime
from model.lampu import lampu_on, lampu_off
#from model.kirim import mail
#from model.camera import VideoCamera as camera


GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)


cap = cv2.VideoCapture(0)

# medifinisikan codec yang dipakai
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

ret, frame = cap.read()
delay = time.sleep(10)

try:
    while ret == True:
        if GPIO.input(pirPin) == GPIO.LOW:
            print "No motion"
=======

try:
    while True:
        if GPIO.input(pirPin) == GPIO.HIGH:
            print ("Gerakan terdeteksi!")
            print ("Kamera mulai merekam...")


            cap = cv2.VideoCapture(0)

            filename = datetime.now().strftime("static/video/%Y-%m-%d_%H.%M.%S.avi")
            codec = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, codec, 20.0, (640, 480))
            ret, frame = cap.read()
            delay = 300
               
            while ret and delay > 0:
                out.write(frame)
                ret, frame = cap.read()
                delay -= 1

#            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
#                time.sleep(3.0)
#                lampu_on()
                

#                time.sleep(10.0)

        else:
            print ("No motion")
##            rekam_off()
>>>>>>> master
            
            lampu.off()
            
<<<<<<< HEAD
        else:
            print "Gerakan terdeteksi!"
            print "Kamera mulai merekam..."
            
            out.write(frame)
            # mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
            # time.sleep(3.0)
            lampu.on()
            # time.sleep(10.0)
            
        time.sleep(0.2)
=======
                      
        
>>>>>>> master
except KeyboardInterrupt:
    GPIO.cleanup()
