import os.path
import json

from model.Patients import Patients
from model.Doctor import Doctors
from model.Appeals import Appeals
from service.ClassListService import ClassListService


class Pan(object):
    def __init__(self, file_name=""):

        self.__patientse = list()
        self.__doctorse = list()
        self.__appealse = list()
        if file_name:
            self.read(file_name)

    # todo Вынести данный метод в соответствующие контроллеры
    def read(self, file_name):
        with open(file_name) as file_input:
            data: dict = json.load(file_input)

        doctors = data.get("doctors")

        for item in doctors:
            doctor = Doctors(item["id"], item["surname"], item["patronymic"], item["specialization"], item["category"])
            self.__doctorse.append(doctor)

        patients = data.get("patients")
        for item in patients:
            patients = Patients(item["id"], item["surname"], item["patronymic"], item["year"])
        self.__patientse.append(patients)

        for item in data["appeals"]:
            appeals = Appeals(item["id"], ClassListService.getByID(self.__doctorse, item["doctors"]),
                              ClassListService.getByID(self.__patientse,item["patients"]),
                              item["date"], item["diagnos"], item["cost"])
            self.__appealse.append(appeals)

    # todo Вынести данный метод в соответствующие контроллеры
    def write(self, file_name):
        if os.path.exists(file_name):
            with open(file_name) as file_input:
                data = json.load(file_input)
        else:
            data = dict()

        data["doctors"] = []
        for item in self.__doctorse:
            doctors = {
                "id": item.getId(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "specialization": item.getSpecialization(),
                "category": item.getCategory()
            }
            data["doctors"].append(doctors)

        data["patients"] = []
        for item in self.__patientse:
            patients = {
                "id": item.getID(),
                "surname": item.getSurname(),
                "patronymic": item.getPatronymic(),
                "year": item.getYear(),
            }
            data["patients"].append(patients)

        data["appeals"] = []
        for item in self.__appealse:
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

    def print(self):
        for item in self.__doctorse, self.__patientse, self.__appealse:
            print(item)


x = Pan("data.json")
x.print()
