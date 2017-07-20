
import RPi.GPIO as GPIO
import cv2
import time
from datetime import datetime
from model.lampu import lampu_on,lampu_off
from model.kirim import kirim
from model.camera import VideoCamera


GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)




while True:
    if GPIO.input(pirPin) == GPIO.HIGH:
        cap = cv2.VideoCapture(0)

        #fps = cap.get(cv2.CAP_PROP_FPS)
        fps = 8

        filename = datetime.now().strftime("static/video/%Y-%m-%d_%H.%M.%S.avi")
	size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, codec, fps, size)
        ret, frame = cap.read()
        delay = 20*fps
        print ("Gerakan terdeteksi!")
        # mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
        
        print ("Kamera mulai merekam...")        
               
        while ret and delay > 0:
            out.write(frame)
            ret, frame = cap.read()
            lampu_on()
            delay -= 1

        kirim('alifpamuji93@gmail.com','ada penyusup boss!!!')

    else:
        print ("No motion")
        lampu_off()
        #GPIO.cleanup()
