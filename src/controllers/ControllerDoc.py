from model.Doctor import Doctors


class ControllerDoc(object):

    def write(self, doctors):
        doctorse = list()
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

    def delet(self, doctors, id):
        doctorse = list()
        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            doctorse.append(doctor)
        return doctorse
