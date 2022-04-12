import json

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class Pan(object):
    def __init__(self, file_name=""):
        controllerDoc = ControllerDoc()
        controllerPat = ControllerPat()
        controllerApp = ControllerApp()
        if file_name:
            with open(file_name) as file_input:
                data: dict = json.load(file_input)
            patientdict = data.get("patients")
            doctordict = data.get("doctors")
            appealdict = data["appeals"]
            self.__patientse = controllerPat.read(patientdict)
            self.__doctorse = controllerDoc.read(doctordict)
            self.__appealse = controllerApp.read(appealdict, self.__patientse, self.__doctorse)

    def read(self):
        for item in self.__patientse, self.__doctorse, self.__appealse:
            print(item)


x = Pan("data.json")
x.read()
