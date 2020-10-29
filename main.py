from flask import Flask
from setup_db import initialize_db
from endpoints.clients import clients
from endpoints.users import users
import logging
import os

DB_SETTINGS = {
    'db': 'thnutrition',
    'host': 'mongodb://localhost/thnutrition'
}
SECRET_KEY = os.urandom(32)

logging.basicConfig(filename='app.log', level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(clients)
app.register_blueprint(users)
app.config['MONGODB_SETTINGS'] = DB_SETTINGS
initialize_db(app)


if __name__ == '__main__':
    app.run(debug=True)
