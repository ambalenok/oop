from model.Patients import Patients


class ControllerPat(object):

    @staticmethod
    def list(patients, patientse):
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
            patientse.append(patients)

    @staticmethod
    def dict(patientse, data):
        for item in patientse:
            patients = {
                "id": item.getID(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "year": item.getYear(),
            }
            data["patients"].append(patients)
