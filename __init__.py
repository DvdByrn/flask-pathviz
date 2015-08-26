from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)


# Minify and combine all assets (js and css)
assets = Environment(app)

css = Bundle(
	'bootstrap/css/bootstrap.min.css',
	Bundle(
		'css/custom.css',
		'escher/builder-1.2.0.css',
		'css/mb_map.css',
		filters='cssmin'
	),
	output='gen/packed.css')

js = Bundle(
	'js/d3-3.5.6.min.js',
	'js/jquery-2.1.4.min.js', 
	'bootstrap/js/bootstrap.min.js',
	Bundle(
		'escher/escher-1.2.0-mb.js',
		'js/mb_map.js',
		filters='jsmin'
	),
	output='gen/packed.js')

assets.register('css_all', css)
assets.register('js_all', js)

# migrations
migrate = Migrate(app, db)

from index import views
from user import views
from net import views

import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(Formatter(
    '%(asctime)s: %(message)s'
))
app.logger.addHandler(handler)
