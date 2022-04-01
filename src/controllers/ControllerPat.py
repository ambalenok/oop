from model.Patients import Patients


class ControllerPat(object):
    @staticmethod
    def ListPat(patients, patientse):
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
            patientse.append(patients)
