from model.Patients import Patients


class ControllerPat(object):

    def write(self, patients):
        patientse = list()

        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
            patientse.append(patients)
        return patientse

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

    def delet(self, list, id):
        for item in list:
            if item.getID() == id:
                del list[1]
                return list
        else:
            return list
