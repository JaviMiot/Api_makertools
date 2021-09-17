from flask import request, jsonify
from . import printer_App
from app.library import PrinterDB
import json

dataBasePrinter = PrinterDB()


@printer_App.route('/settings', methods=['GET', 'POST'])
def get_settings():

    if request.method == 'POST':
        return jsonify(Updated=dataBasePrinter.update_printer_settings(request.json)), 200

    printer_settings = dataBasePrinter.get_printer_settings()
    return jsonify(json.loads(printer_settings))
