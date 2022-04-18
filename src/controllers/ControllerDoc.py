from controllers.BasiController import BasiController
from model.Doctor import Doctors


class ControllerDoc(BasiController):

    def read(self):
        doctorse = list()
        basicontroller = BasiController()
        doctors = basicontroller.baza('doc')
        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            doctorse.append(doctor)
        return doctorse

    def dict(self, doctorse, data):
        for item in doctorse:
            doctors = {
                "id": item.getId(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "specialization": item.getSpecialization(),
                "category": item.getCategory()
            }
            data["doctors"].append(doctors)

    def delet(self, list, id):
        for item in list:
            if item.getID() == id:
                del list[id - 1]
                return list
        else:
            return list
