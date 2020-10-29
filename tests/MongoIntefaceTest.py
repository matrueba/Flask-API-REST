from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask import Flask


app = Flask(__name__)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
