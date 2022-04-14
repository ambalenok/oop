import json

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class BasiController(object):
    def read(self, file_name):
        if file_name:
            with open(file_name) as file_input:
                data: dict = json.load(file_input)
                controllerPat = ControllerPat()
                controllerDoc = ControllerDoc()
                controllerApp = ControllerApp()
            patientdict = data.get("patients")
            doctordict = data.get("doctors")
            appealdict = data["appeals"]
            self.__patientse = controllerPat.read(patientdict)
            self.__doctorse = controllerDoc.read(doctordict)
            self.__appealse = controllerApp.read(appealdict, self.__patientse, self.__doctorse)
            return self.__patientse + self.__doctorse + self.__appealse
