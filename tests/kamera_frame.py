import cv2
from  datetime import datetime
import time

cameraCapture = cv2.VideoCapture(0)

fps = cv2.CAP_PROP_FPS # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
	int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")

codecs = cv2.VideoWriter_fourcc(*'XVID')

videoWriter = cv2.VideoWriter(filename, codecs, fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
delay = time.sleep(10)

while success and delay > 0:
	videoWriter.write(frame)
	success, frame = cameraCapture.read()
	delay -= 1