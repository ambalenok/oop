from controllers.BaseController import BaseController
from model.Patients import Patients


class ControllerPat(BaseController):

    def read(self):
        patients = self.getDataByKey('pat')
        list = self.read2(patients, Patients)
        return list

    def dict(self, patientse, data):
        for item in patientse:
            patients = {
                "id": item.getID(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "year": item.getYear(),
            }
            data["patients"].append(patients)

    def delet(self, list, id):
        for item in list:
            if item.getID() == id:
                del list[id % 10]
                return list
        else:
            return list
