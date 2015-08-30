from flask_app import app
from flask import render_template, session, request, json, jsonify
from user.decorators import login_required

@app.route('/map')
@login_required
def map():
	return render_template('net/map.html', username=session['username'])

@app.route('/_flux_data', methods=["POST"])
def flux_data():
    fluxlist = json.loads(request.args.get('fluxlist'))
    fluxlist_pretty = json.dumps(fluxlist, sort_keys=True, indent=4)
    print fluxlist_pretty