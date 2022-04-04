from model.Patients import Patients


class ControllerPat(object):
    # todo
    @staticmethod
    def List(patients, patientse):
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
            patientse.append(patients)

    # todo
    @staticmethod
    def Dict(patientse, data):
        for item in patientse:
            patients = {
                "id": item.getID(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "year": item.getYear(),
            }
            data["patients"].append(patients)