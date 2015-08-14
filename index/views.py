from flask_app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/welcome')
def index():
	return render_template('index.html')
