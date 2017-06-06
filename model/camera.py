import RPi.GPIO as GPIO
import cv2
#import numpy
import time
from datetime import datetime
from lampu import lampu_on, lampu_off
#from kirim import mail
#from camera import VideoCamera as camera


GPIO.setmode(GPIO.BCM)
pirPin = 18
GPIO.setup(pirPin, GPIO.IN)


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
    
    def rekam_app(self):
        while True:
            if GPIO.input(pirPin) == GPIO.HIGH:
                print ("Gerakan terdeteksi!")
    #            mail("alifpamuji93@gmail.com", "subjek", "halo", "README.md")
                lampu_on()
                print ("Kamera mulai merekam...")


                fps = 20

                filename = datetime.now().strftime("static/video/%Y-%m-%d_%H.%M.%S.mp4")
                codec = cv2.VideoWriter_fourcc(*'H264')
                out = cv2.VideoWriter(filename, codec, fps, (640, 480))
                ret, frame = self.video.read()
                delay = 20*fps
                   
                while ret and delay > 0:
                    out.write(frame)
                    ret, frame = self.video.read()
                    delay -= 1
                    
            else:
                print ("No motion")
                lampu_off()
         
    def __del__(self):
        self.video.release()
        self.video.destroyAllWindows()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
