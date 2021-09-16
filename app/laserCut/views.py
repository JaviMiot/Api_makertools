from flask import request, jsonify
from . import laserCut_App
from app.library import LaserCutDB

db_Laser = LaserCutDB()


@laserCut_App.route('/settings', methods=['GET', 'POST'])
def get_settings():

    if request.method == 'POST':
        return jsonify(Updated=db_Laser.update_laserCut_settings(request.json)), 200

    laser_cut_settings = db_Laser.get_laserCut_settings()
    return laser_cut_settings
