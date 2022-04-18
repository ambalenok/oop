from controllers.BasiController import BasiController
from model.Patients import Patients


class ControllerPat(BasiController):

    def read(self):
        patientse = list()
        basicontroller = BasiController()
        patients = basicontroller.baza('pat')
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
            patientse.append(patients)
        return patientse

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
