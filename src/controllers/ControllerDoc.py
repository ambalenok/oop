from model.Doctor import Doctors


class ControllerDoc(object):
    @staticmethod
    def ListDoc(doctors, doctorse):
        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            doctorse.append(doctor)
