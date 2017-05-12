import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, codec, 20.0, (640, 480))


ret, frame = cap.read()
while (cap.isOpened()):
    out.write(frame)


    
