import cv2
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
pirPin = 18
relayPin = 17

GPIO.setup(pirPin, GPIO.IN)
   
while True:


    if GPIO.input(pirPin) == GPIO.HIGH:
        print("Gerakan terdeteksi!")
        print("Kamera mulai merekam...")

        GPIO.setwarnings(False)
        GPIO.setup(relayPin, GPIO.OUT)


        cap = cv2.VideoCapture(0)

        filename = datetime.now().strftime("../static/video/%Y-%m-%d_%H.%M.%S.avi")
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, codec, 20.0, (640, 480))
        ret, frame = cap.read()

        while (cap.isOpened()):
            out.write(frame)
            GPIO.setup(relayPin, GPIO.OUT) 
        
##        cap.release()
##        out.release()

    else:     
        print("No Motion")

        GPIO.cleanup(relayPin)
        
