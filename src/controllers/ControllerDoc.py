from controllers.BaseController import BaseController
from model.Doctor import Doctors


class ControllerDoc(BaseController):
    def __init__(self):
        super().__init__('doc')

    def getModel(self, item):
        return Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])

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
##