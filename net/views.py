from flask_app import app
from flask import render_template, session
from user.decorators import login_required

@app.route('/map')
@login_required
def map():
	return render_template('net/map.html', username=session['username'])
