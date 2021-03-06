# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from flask_app import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Instantiate the server with the required flags.
# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = app.config['DEBUG'],
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()