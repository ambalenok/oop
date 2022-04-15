import json

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class BasiController(object):
    def __init__(self, file_name=""):
        with open(file_name) as file_input:
            data: dict = json.load(file_input)

        controllerPat = ControllerPat()
        controllerDoc = ControllerDoc()
        controllerApp = ControllerApp()
        patientdict = data.get("patients")
        doctordict = data.get("doctors")
        appealdict = data["appeals"]

        patientse = controllerPat.read(patientdict)
        doctorse = controllerDoc.read(doctordict)
        appealse = controllerApp.read(appealdict, patientse, doctorse)
        self.__list = patientse + doctorse + appealse

    def read(self):
        return self.__list
