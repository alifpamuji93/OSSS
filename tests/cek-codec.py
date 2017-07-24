import cv2
import time

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS) # default fps with openCV is 5


# count = time.sleep(180)

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, size)

for i in xrange(20):
	ret, frame = cap.read()
	out.write(frame)

# success, frame = cap.read()
# numFramesRemaining = 20 * fps - 1

# while success and numFramesRemaining > 0:
	
# 	success, frame = cap.read()
# 	out.write(frame)
# 	numFramesRemaining -= 1