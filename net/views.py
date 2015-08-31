from flask_app import app
from flask import render_template, session, request, json, jsonify
from user.decorators import login_required
from datetime import datetime
import os

@app.route('/map')
@login_required
def map():
	return render_template('net/map.html', username=session['username'])

@app.route('/_flux_data', methods=["POST"])
def flux_data():
	if request.method == "POST":
 		fluxlist = json.loads(request.data)
		fluxlist_pretty = json.dumps(fluxlist, sort_keys=True, indent=4)

		# Save the data in the uploads folder
		timestamp = datetime.utcnow().isoformat()
		root = os.getcwd()
		fileName = root + "/" + app.config['UPLOAD_FOLDER'] + timestamp + ".txt"
		with open(fileName, "w+") as fo:
			fo.write(fluxlist_pretty)
 		return str(fluxlist_pretty)