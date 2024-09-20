from flask import Flask
from .models import base_model
from .session.session import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    init_db(app)
    return app
