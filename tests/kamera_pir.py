import cv2
import time
from datetime import datetime
import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
pirPin = 18
relayPin = 17
# GPIO.setup(pirPin, GPIO.IN)

state = False
val = False

GPIO.setmode(GPIO.BCM)	# Change this if using GPIO numbering
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)	# Set relay as output

cap = cv2.VideoCapture(0)

# medifinisikan codec yang dipakai
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))


ret, frame = cap.read()

# while ret:
# 	out.write(frame)
# 	ret, frame = cap.read()



while True:
	GPIO.setup(pirPin, GPIO.IN)
	val = GPIO.input(pirPin)		# read input value
	if (val == True):		# check if the input is HIGH
		GPIO.output(relayPin, True)	# turn LED ON
		if (state == False):
			# ON
			out.write(frame)
			ret, frame = cap.read()
			state = True
	else:
		GPIO.setup(relayPin, GPIO.OUT)	# Set relay as output
		GPIO.output(relayPin, False)	# turn LED OFF
		if (state == True):
			# OFF
			time.sleep(2)
			state = False;
			GPIO.cleanup()