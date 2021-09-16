import os
from pymongo import MongoClient
from bson.json_util import dumps

urlMongo = os.environ.get('URL_MONGO')
database = os.environ.get('DB_NAME')


class MongoDB:

    __instance = None

    @staticmethod
    def getInstance():
        if MongoDB.__instance == None:
            MongoDB()
        return MongoDB.__instance

    def __init__(self):
        self.client = MongoClient(urlMongo)
        self.db = self.client[database]
        MongoDB.__instance = self


class PrinterDB(MongoDB):

    def __init__(self):
        super().__init__()

    def get_printer_settings(self):
        return dumps(self.db.toolsSettings.find_one({'name': '3d Printer Settings'}))

    def update_printer_settings(self, setting):
        data_settings = setting['Settings']
        query = {'name': setting['name']}

        data_update = {
            "Settings.pla_cost": data_settings['pla_cost'],
            "Settings.energy": data_settings['energy'],
            "Settings.power_printer": data_settings['power_printer'],
            "Settings.printer_cost": data_settings['printer_cost'],
            "Settings.amortization": data_settings['amortization'],
            "Settings.active_days": data_settings['active_days'],
            "Settings.hours_in_day": data_settings['hours_in_day'],
            "Settings.fail_percent": data_settings['fail_percent'],
            "Settings.operator_cost_by_hour": data_settings['operator_cost_by_hour'],
            "Settings.preparation_time": data_settings['preparation_time'],
            "Settings.post_processed_time": data_settings['post_processed_time'],
        }

        return str(self.db.toolsSettings.update_one(query, {'$set': data_update}).modified_count)


class LaserCutDB(MongoDB):

    def __init__(self):
        super().__init__()

    def get_laserCut_settings(self):
        return dumps(self.db.toolsSettings.find_one({'name': 'Laser cut Settings'}))

    def update_laserCut_settings(self, setting):
        data_settings = setting['Settings']
        query = {'name': setting['name']}

        data_update = {
            "Settings.power": data_settings['power'],
            "Settings.voltaje": data_settings['voltaje'],
            "Settings.power_consumption_all": data_settings['power_consumption_all'],
            "Settings.lighting_energy_consumptio": data_settings['lighting_energy_consumptio'],
            "Settings.power_cost": data_settings['power_cost'],
            "Settings.power_cost_in_one_hour": data_settings['power_cost_in_one_hour'],
        }

        return str(self.db.toolsSettings.update_one(query, {'$set': data_update}).modified_count)


if __name__ == '__main__':
    dataBase1 = MongoDB.getInstance()
    dataBase2 = MongoDB.getInstance()
    print(dataBase1 == dataBase2)
    printer = PrinterDB()
    laser = LaserCutDB()
    print(printer.getInstance() == laser.getInstance())
