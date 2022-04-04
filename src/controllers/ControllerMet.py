import json
import os

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class ControllerMet(object):

    def read(file_name, doctorse, patientse, appealse):
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
        doctors = data.get("doctors")
        ControllerDoc.list(doctors, doctorse)
        patients = data.get("patients")
        ControllerPat.list(patients, patientse)
        appeals = data["appeals"]
        ControllerApp.list(appeals, appealse, doctorse, patientse)

    def write(file_name, doctorse, patientse, appealse):
        if os.path.exists(file_name):
            with open(file_name) as file_input:
                data = json.load(file_input)
        else:
            data = dict()

        data["doctors"] = []
        ControllerDoc.dict(doctorse, data)

        data["patients"] = []
        ControllerPat.dict(patientse, data)

        data["appeals"] = []
        ControllerApp.dict(appealse, data)

        with open(file_name, "w") as file_output:
            json.dump(data, file_output)

    def print(self):
        for item in self.__doctorse, self.__patientse, self.__appealse:
            print(item)

    def delete(self):
        pass
