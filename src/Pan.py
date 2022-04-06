import json

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class Pan(object):
    def __init__(self, file_name=""):

        if file_name:
            with open(file_name) as file_input:
                data: dict = json.load(file_input)
            patientdict = data.get("patients")
            doctordict = data.get("doctors")
            appealdict = data["appeals"]
            self.__patientse = ControllerPat.list(patientdict)
            self.__doctorse = ControllerDoc.list(doctordict)
            self.__appealse = ControllerApp.list(appealdict, self.__patientse, self.__doctorse)

    def print(self):
        for item in self.__doctorse, self.__patientse, self.__appealse:
            print(item)


x = Pan("data.json")
x.print()
