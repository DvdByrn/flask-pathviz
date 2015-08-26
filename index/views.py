from flask_app import app
from flask import render_template, session
from user.decorators import login_required

@app.route('/')
@app.route('/welcome')
@login_required
def index():
	return render_template('index/index.html', username=session['username'])
