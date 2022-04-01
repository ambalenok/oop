import json

from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class ControllerMet(object):

    def read(file_name, doctorse, patientse, appealse):
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
        doctors = data.get("doctors")
        ControllerDoc.ListDoc(doctors, doctorse)
        patients = data.get("patients")
        ControllerPat.ListPat(patients, patientse)
        appeals = data["appeals"]
        ControllerApp.ListApp(appeals, appealse, doctorse, patientse)

    def delete(self):
        pass
