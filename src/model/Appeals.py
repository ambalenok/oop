class Appeals(object):
    def __init__(self, id, doctors, patients, date, diagnos, cost):
        self.__id = id
        self.__doctors = doctors
        self.__patients = patients
        self.__date = date
        self.__diagnos = diagnos
        self.__cost = cost

    def setID(self, id):
        self.__id = id

    def setDoctors(self, doctors):
        self.__doctors = doctors

    def setPatients(self, patients):
        self.__patients = patients

    def setDate(self, date):
        self.__date = date

    def setDiagnos(self, diagnos):
        self.__diagnos = diagnos

    def setCost(self, cost):
        self.__cost = cost

    def getID(self):
        return self.__id

    def getDoctors(self):
        return self.__doctors

    def getPatients(self):
        return self.__patients

    def getDate(self):
        return self.__date

    def getDiagnos(self):
        return self.__diagnos

    def getCost(self):
        return self.__cost

    def __repr__(self):
        return (f"ID: {self.__id}\n idDoctors: {self.__doctors}\n idPatients:{self.__patients}\n"
                f""f"Date: {self.__date}\n Diagnos: {self.__diagnos}\n Cost: {self.__cost}")
