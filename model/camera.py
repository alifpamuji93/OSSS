
from __future__ import (
    unicode_literals,
    print_function,
    absolute_import,
    division,
)

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

	

	def filename(self):
		self.dirName = 'static/video'
		self.filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
		return self.dirName + self.filename

	def codecName(self, value):
		if self.codecName is not None:
			self.codecName = 'X', 'V', 'I', 'D'
			return self.codecName


	def codec(self):
		self.codec = cv2.VideoWriter_fourcc(self.codecName)

	def fps(self, value):
		if self.fps != value:
			self.fps = cv2.CAP_PROP_FPS

	def resolution(self, value):
		if self.resolution is not None:
			self.resolution = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
	int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

   
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    
    
    	

    def rekam(self):
    	ret, frame = self.video.read()
    	if ret == True:
			# write the flipped frame
			
			self.video.release()
			self.video.release()
			cv2.destroyAllWindows()


