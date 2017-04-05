#!/usr/bin/env python
#
# Project: Video Streaming with Flask
# Author: Log0 <im [dot] ckieric [at] gmail [dot] com>
# Date: 2014/12/21
# Website: http://www.chioka.in/
# Description:
# Modified to support streaming out with webcams, and not just raw JPEGs.
# Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
# Credits: http://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.
from flask import Flask, request, url_for, redirect, render_template, Response
from camera import VideoCamera

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/daftar_video')					
def daftar_video():
    return render_template('daftar_video.html')
	
@app.route('/kontrol_gpio')
def kontrol_gpio():
    return render_template('kontrol_gpio.html')


     
@app.route('/gpio_on')
def gpio_on():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)

    return render_template('gpio_on.html')

@app.route('/gpio_off')
def gpio_off():
    GPIO.cleanup()
    return render_template('gpio_off.html')



@app.route('/video_streaming')
def video_streaming():
    return render_template('video_streaming.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
					


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
