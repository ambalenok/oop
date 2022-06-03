from controllers.BaseController import BaseController
from model.Patients import Patients

#
class ControllerPat(BaseController):
    # def __init__(self, id, surname, patronymic, year):
    # self.year = year
    # super.__init__(id, surname, patronymic)

    def read(self):
        item = super().read('pat')
        return item

    def getModelP(self, item):

        return Patients(item["id"], item["surname"], item["patronymic"], item["year"])

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
