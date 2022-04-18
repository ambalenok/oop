import json
import configparser


class BaseController(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("settings.conf")

    def getDataByKey(self, key):
        file_name = self.config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]
