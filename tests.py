# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask_app import app, db

# Need to add all models for db.create_all to work.
from user.models import *

# Test user login/logout
class UserTest(unittest.TestCase):
	def setUp(self):
		self.db_uri = 'sqlite:///%s.db' % (app.config['DATABASE_NAME'])
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DATABASE_NAME'] = 'test_metmodviz'
		# app.config['SQL_ALCHEMY_DATABASE_URI'] = self.db_uri + app.config['DATABASE_NAME']
		# engine = sqlalchemy.create_engine(self.db_uri)
		# conn = engine.connect()
		# conn.execute('commit')
		# conn.execute("CREATE DATABASE " + app.config['DATABASE_NAME'])
		db.create_all()
		# conn.close()
		self.app = app.test_client()

	def tearDown(self):
		db.session.remove()
		engine = sqlalchemy.create_engine(self.db_uri)
		# conn = engine.connect()
		# conn.execute('commit')
		# conn.execute("DROP DATABASE " + app.config['DATABASE_NAME'])
		# conn.close()

if __name__ == "__main__":
    unittest.main()