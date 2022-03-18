class Shared(object):
    def __init__(self, id, surname, patronymic):
        self.__id = id
        self.__surname = surname
        self.__patronymic = patronymic

    def setID(self, id):
        self.__id = id

    def setSurname(self, surname):
        self.__surname = surname

    def setPatronymic(self, patronymic):
        self.__patronymic = patronymic

    def getID(self):
        return self.__id

    def getSurname(self):
        return self.__surname

    def getPatronymic(self):
        return self.__patronymic
# --
