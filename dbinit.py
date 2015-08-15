import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_app import app
import sqlalchemy

# try:

# db_uri = 'sqlite:///%s.db' % (app.config['DATABASE_NAME'])
# engine = sqlalchemy.create_engine(db_uri)
# conn = engine.connect()
# conn.execute('commit')
# conn.execute("DROP DATABASE " + app.config['DATABASE_NAME'])
# conn.execute("CREATE DATABASE " + app.config['DATABASE_NAME'])
# conn.close()

# except:
# 	print "Database exists"

from flask_app import db

# # Add all models here
# from user.models import *

# db.create_all()
