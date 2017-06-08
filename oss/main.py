
#!/usr/bin/env python
#

from flask import Flask, request, url_for, redirect, render_template, Response
from model.camera import VideoCamera
from model.lampu import lampu_on, lampu_off

# Import lib login page
from flask import flash, redirect, request, session, abort
import os

video_dir = 'static/video'


app = Flask(__name__)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'al' and request.form['username'] == 'alif':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    return render_template('index.html')
		
@app.route('/daftar_video')
def daftar_video():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        video_files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
        video_files_number = len(video_files)
        return render_template("daftar_video.html",
            title = 'Video list',
            video_files_number = video_files_number,
            video_files = video_files)

@app.route('/play/<filename>.html')
def song(filename):
    return render_template('play.html',
                        title = 'play',
                        filename = filename)
	
@app.route('/kontrol_gpio')
def kontrol_gpio():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    return render_template('kontrol_gpio.html')
		
@app.route('/gpio_on')
def gpio_on():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    lampu_on()
	    return render_template('gpio_on.html')

@app.route('/gpio_off')
def gpio_off():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    lampu_off()
            return render_template('gpio_off.html')

@app.route('/video_streaming')
def video_streaming():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
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
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    return render_template('about.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port=5000, debug=True)
