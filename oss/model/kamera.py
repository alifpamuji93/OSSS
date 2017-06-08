import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
# medifinisikan codec yang dipakai
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))
	
def rekam_on():
	

    while (cap.isOpened()):
	ret, frame = cap.read()

	out.write(frame)

	gray = cv2.cv.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF  == ord('q'):
	    break

def rekam_off():
	cap.release()
	out.release()
	cap.destroyAllWindows()


