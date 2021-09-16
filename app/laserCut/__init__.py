from flask import Blueprint

laserCut_App = Blueprint('lasercut',__name__, url_prefix='/lasercut')

#* import views

from . import views