import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

# medifinisikan codec yang dipakai
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))


ret, frame = cap.read()

while ret:
	out.write(frame)
	ret, frame = cap.read()