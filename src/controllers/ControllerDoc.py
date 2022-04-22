from controllers.BaseController import BaseController
from model.Doctor import Doctors


class ControllerDoc(BaseController):

    def read(self):
        item = super().read('doc', Doctors)
        return item

    def getModelD(self, item):
        jojo = (item["specialization"], item["category"])

        return jojo

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
