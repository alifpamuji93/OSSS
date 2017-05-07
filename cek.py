from flask import Flask, request, url_for, redirect, render_template, Response
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def index():
	return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)