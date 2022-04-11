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
            self.__patientse = controllerPat.write(patientdict)
            self.__doctorse = controllerDoc.write(doctordict)
            self.__appealse = controllerApp.write(appealdict, self.__patientse, self.__doctorse)
            id = 51
            self.__patientse = controllerPat.delet(self.__patientse, id)

    def read(self):
        for item in self.__patientse:
            print(item)


x = Pan("data.json")
x.read()
