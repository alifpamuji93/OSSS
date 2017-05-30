import cv2
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pirPin = 18
relayPin = 17

GPIO.setup(pirPin, GPIO.IN)

cap = cv2.VideoCapture(0)


      
while True:


    if GPIO.input(pirPin) == GPIO.HIGH:
        print("Gerakan terdeteksi!")
        print("Kamera mulai merekam...")        

        filename = datetime.now().strftime("../static/video/%Y-%m-%d_%H.%M.%S.avi")
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, codec, 20.0, (640, 480))

        while (cap.isOpened()):
            ret, frame = cap.read()
            out.write(frame)
           
                
        time.sleep(3.0)
        print("Lampu menyala")        
        GPIO.setup(relayPin, GPIO.OUT)
                         
        time.sleep(10.0)
            
        
##        cap.release()
##        out.release()

    else:     
        print("No Motion")


        GPIO.cleanup(relayPin)
        
