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


try:
    while True:
        if GPIO.input(pirPin) == GPIO.HIGH:
            print ("Gerakan terdeteksi!")
            print ("Kamera mulai merekam...")


            cap = cv2.VideoCapture(0)
            fps = 20

            filename = datetime.now().strftime("static/video/%Y-%m-%d_%H.%M.%S.avi")
            codec = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, codec, fps, (640, 480))
            ret, frame = cap.read()
            delay = 20*fps
               
            while ret and delay > 0:
                out.write(frame)
                ret, frame = cap.read()
                delay -= 1

#            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
#                time.sleep(3.0)
                lampu_on()
                

#                time.sleep(10.0)

        else:
            print ("No motion")
##            rekam_off()
            
            lampu_off()
            
                      
        
except KeyboardInterrupt:
    GPIO.cleanup()
