import numpy
import cv2

capture = cv2.VideoCapture(0)
while True:

    frame = cv2.QueryFrame(capture)
    aframe = numpy.asarray(frame[:,:])
    cv2.imshow("w1", aframe)
    c = cv.WaitKey(5)
    if c == 110: #to quit, the 'n' key is pressed
        exit()