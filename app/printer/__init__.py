from flask import Blueprint

printer_App = Blueprint('printer', __name__, url_prefix='/printer')

# * get views
from . import views
