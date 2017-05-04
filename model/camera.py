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
        self.filename = None
        self.codecName = None
        self.codec = None
        self.fps = None
        self.resolution = None
        self.output = None
        self.capture = None  

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

	def capture(self):
		self.capture = cv2.VideoCapture(0)

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

    def output(self):
    	self.output = cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)
    	return self.output

    def saveFile(self):
    	self.filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.avi")
    	self.dirName = 'static/video'
    	return self.dirName + self.filename
    	

    def rekam(self):
    	ret, frame = self.capture.read()
    	if ret == True:
			# write the flipped frame
			self.video.write(frame)
			self.timer -= 0
			self.video.release()
			self.video.release()
			cv2.destroyAllWindows()

        
class CaptureManager(object):
	def __init__(self, capture, previewWindowManager = None,
		shouldMirrorPreview = False):
            
            self.previewWindowManager = previewWindowManager
            self.shouldMirrorPreview = shouldMirrorPreview
            self._capture = capture
            self._channel = 0
            self._enteredFrame = False
            self._frame = None
            self._imageFilename = None
            self._videoFilename = None
            self._videoEncoding = None
            self._videoWriter = None
            self._startTime = None
            self._framesElapsed = long(0)
            self._fpsEstimate = None


	@property
	def channel(self):
		return self._channel

	@channel.setter
	def channel(self, value):
		if self._channel != value:
			self._channel = value
			self._frame = None

	@property
	def frame(self):
		if self._enteredFrame and self._frame is None:
			_, self._frame = self._capture.retrieve(
				channel = self.channel)
			return self._frame

	@property
	def isWritingImage(self):
		return self._imageFilename is not None

	@property
	def isWritingVideo(self):
		return self._videoFilename is not None

	def enterFrame(self):
		"""Capture the next frame, if any."""
		# But first, check that any previous frame was exited.
		assert not self._enteredFrame, \
		'previous enterFrame() had no matching exitFrame()'
		if self._capture is not None:
			self._enteredFrame = self._capture.grab()

	def exitFrame(self):
		"""Draw to the window. Write to files. Release the frame."""
		# Check whether any grabbed frame is retrievable.
		# The getter may retrieve and cache the frame.
		if self.frame is None:
			self._enteredFrame = False
			return
			
		# Update the FPS estimate and related variables.
		if self._framesElapsed == 0:
			self._startTime = time.time()
		else:
			timeElapsed = time.time() - self._startTime
			self._fpsEstimate = self._framesElapsed / timeElapsed
			self._framesElapsed += 1


		# Draw to the window, if any.
		if self.previewWindowManager is not None:
			if self.shouldMirrorPreview:
				mirroredFrame = numpy.fliplr(self._frame).copy()
				self.previewWindowManager.show(mirroredFrame)
			else:
				self.previewWindowManager.show(self._frame)

		# Write to the image file, if any.
		if self.isWritingImage:
			cv2.imwrite(self._imageFilename, self._frame)
			self._imageFilename = None


		# Write to the video file, if any.
		self._writeVideoFrame()
		
		# Release the frame.
		self._frame = None
		self._enteredFrame = False
