from Shared import Shared


class Doctors(Shared):
    def __init__(self, id, surname, patronymic, specialization, category):
        super().__init__(id, surname, patronymic)
        self.__specialization = specialization
        self.__category = category

    def setSpecialization(self, specialization):
        self.__specialization = specialization

    def setCategory(self, category):
        self.__category = category

    def getSpecialization(self):
        return self.__specialization

    def getCategory(self):
        return self.__category

    def __repr__(self):
        return (f"ID: {self.getID()}\n Имя пациента: {self.getSurname()}\n Фамилия: {self.getPatronymic()}\n "
                f" Специальность:{self.__specialization}\n Категория:{self.__category}\n")
