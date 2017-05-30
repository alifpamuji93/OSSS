import RPi.GPIO as GPIO
import time
import cv2
from datetime import datetime

GPIO.setmode(GPIO.BCM)

pirPin = 18
GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
camera = cv2.VideoCapture(0)
counter = 1
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480), counter)
success, frame = camera.read()

while True:
	if GPIO.input(pirPin) == GPIO.LOW:
		try:
			camera.write()
			time.sleep(1)
			camera.read()
			counter = counter + 1
			camera.release()
		except:
			camera.release()
	time.sleep(3)