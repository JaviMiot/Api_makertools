from flask import Flask
from .config import Config

# * Blueprints

from app.printer import printer_App
from app.laserCut import laserCut_App


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(printer_App)
    app.register_blueprint(laserCut_App)
    return app
