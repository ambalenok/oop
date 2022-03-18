from model.Shared import Shared

class Patients(Shared):
    def __init__(self, id, surname, patronymic, year):
        super().__init__(id, surname, patronymic)
        self.__year = year

    def setYear(self, year):
        self.__year = year

    def getYear(self):
        return self.__year

    def __repr__(self):
        return (f"ID: {self.getID()}\n Имя пациента: {self.getSurname()}\n Фамилия: {self.getPatronymic()}\n "
                f"Лет:{self.__year}")
