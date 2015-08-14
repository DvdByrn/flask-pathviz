from flask_app import app

@app.route('/login')
def login():
	return "User Login"
