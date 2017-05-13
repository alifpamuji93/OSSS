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

filename = datetime.now().strftime("../static/video/%Y-%m-%d_%H.%M.%S.avi")
# Define the codec and create VideoWriter object
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename,codec, 20.0, (640,480))

while GPIO.input(pirPin) == GPIO.HIGH:
	ret, frame = cap.read()
	if ret==True:
		# write the flipped frame
		out.write(frame)
		print("Lampu menyala")
		GPIO.setup(relayPin, GPIO.OUT)
		# cv2.imshow('frame',frame)
		if cv2.waitKey(1) & GPIO.input(pirPin) == GPIO.LOW:
			break
	else:
		break
		GPIO.cleanup(relayPin)

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()