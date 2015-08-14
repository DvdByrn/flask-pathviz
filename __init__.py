from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from index import views
from user import views
