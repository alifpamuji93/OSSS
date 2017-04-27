#!/usr/bin/env python

from flask import Flask, request, redirect, render_template, Response
from camera import VideoCamera

import os
import sys

video_dir = 'static/video'

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/daftar_video')
def video():
    video_files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
    video_files_number = len(video_files)
    return render_template("video.html",
        title = 'Video list',
        video_files_number = video_files_number,
        video_files = video_files)

@app.route('/play/<filename>.html')
def song(filename):
    return render_template('play.html',
                        title = 'play',
                        filename = filename)

@app.route('/video_streaming')
def camera():
    return render_template('index.html', title = 'Lihat ruangan')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


    
@app.route('/kontrol_gpio')
def kontrol_gpio():
    return render_template('kontrol_gpio.html')
                    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gpio_on')
def gpio_on():
    return render_template('gpio_on.html')

@app.route('/gpio_off')
def gpio_off():
    return render_template('gpio_off.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
