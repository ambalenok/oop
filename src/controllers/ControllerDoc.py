from model.Doctor import Doctors


class ControllerDoc(object):
    # todo
    @staticmethod
    def List(doctors, doctorse):
        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            doctorse.append(doctor)

    # todo
    @staticmethod
    def Dict(doctorse, data):
        for item in doctorse:
            doctors = {
                "id": item.getId(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "specialization": item.getSpecialization(),
                "category": item.getCategory()
            }
            data["doctors"].append(doctors)
