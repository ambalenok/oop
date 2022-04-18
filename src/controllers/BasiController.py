import json
import configparser


config = configparser.ConfigParser()
config.read("settings.conf")


class BasiController(object):
    def baza(self,key):
        file_name = config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]


