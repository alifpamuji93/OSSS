

import cv2
import numpy
import time
from datetime import datetime

class VideoCamera(object):
    """ video streaming dengan openCV
        =============================

        dengan menggunakan openCV kamera mmengcapture /mengambil gambar
        melalui device dengan inisialisasi 0. 

     """
    def __init__(self):
        """
        Using OpenCV to capture from device 0. If you have trouble capturing
        from a webcam, comment the line below out and use a video file
        instead.
        """
        self.video = cv2.VideoCapture(0)
        """
        If you decide to use video.mp4, you must have this file in the folder
        as the main.py.
       """
        # self.videomp4 = cv2.VideoCapture('video.mp4')        
       
    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def read(self):
        success, image =self.video.read()
        return

    def rekam(self):
        while self.ret and self.delay > 0:
            self.ret, self.frame = self.video.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv2.imshow('frame',gray)
            self.delay -= 1
        return

camera = VideoCamera()
camera.rekam()