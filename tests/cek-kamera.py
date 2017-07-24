# import numpy as np
import cv2
# from datetime import datetime 

cap = cv2.VideoCapture(1)

# name = datetime.now().strftime("static/video/%Y-%m-%d_%H.%M.%S.avi")
# codec = cv2.VideoWriter_fourcc(*'XVID')
# size = (640, 480)
# fps = cap.get(cv2.CAP_PROP_FPS)

# out = cv2.VideoWritter(name, codec, fps, size)
k = cv2.waitKey(0) & 0xFF

while True:
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display the resulting frame
	cv2.imshow('cek foto', gray)
	if k == ord('q'):
		cv2.destroyAllWindows()
	elif k == ord('s'):
		cv2.imwrite('foto.png', frame)
		cap.release()
		cv2.destroyAllWindows()
# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()