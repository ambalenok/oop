import json
import os.path
from model.Patients import Patients
from model.Doctor import Doctors
from model.Appeals import Appeals
from service.ClassListService import ClassListService


class ControllerMet(object):

    def read(file_name, doctorse, patientse, appealse):
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
        doctors = data.get("doctors")

        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            doctorse.append(doctor)

        patients = data.get("patients")
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
        patientse.append(patients)

        for item in data["appeals"]:
            appeals = Appeals(item["id"], ClassListService.getByID(doctorse, item["doctors"]),
                              ClassListService.getByID(patientse, item["patients"]),
                              item["date"], item["diagnos"], item["cost"])
            appealse.append(appeals)

    def write(file_name, doctorse, patientse, appealse):
        if os.path.exists(file_name):
            with open(file_name) as file_input:
                data = json.load(file_input)
        else:
            data = dict()

        data["doctors"] = []
        for item in doctorse:
            doctors = {
                "id": item.getId(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "specialization": item.getSpecialization(),
                "category": item.getCategory()
            }
            data["doctors"].append(doctors)

        data["patients"] = []
        for item in patientse:
            patients = {
                "id": item.getID(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "year": item.getYear(),
            }
            data["patients"].append(patients)

        data["appeals"] = []
        for item in appealse:
            appeal = {
                "id": item.getId(),
                "doctorse": item.getDoctors(),
                "patientse": item.getPatients(),
                "date": item.getDate(),
                "diagnos": item.getDiagnos(),
                "cost": item.getCost()
            }
            data["appeals"].append(appeal)
        with open(file_name, "w") as file_output:
            json.dump(data, file_output)

    def delete(self):
        pass
