import json
import configparser
from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp

config = configparser.ConfigParser()
config.read("settings.conf")


class BasiController(object):
    def baza(self, key):
        file_name = config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]

    def read(self):
        controllerPat = ControllerPat()
        controllerDoc = ControllerDoc()
        controllerApp = ControllerApp()

        patientse = controllerPat.read()
        doctorse = controllerDoc.read()
        appealse = controllerApp.read(patientse, doctorse)
        self.__list = patientse + doctorse + appealse
        return self.__list
