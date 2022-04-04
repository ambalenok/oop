from controllers.ControllerMet import ControllerMet


class Pan(object):
    def __init__(self, file_name=""):
        # todo Не верная логика работы. Ты создаёшь пустые списки и передаёшь их в метод read.
        #  Должно быть наоборот. Ты из метода read должен получить соответствующий список, от соответствующего
        #  контроллера, т.е.: self.__patientse = controllerPat.read().
        #  Соответственно, класс ControllerPat должен быть проинициализирован заранее.
        self.__patientse = list()
        self.__doctorse = list()
        self.__appealse = list()
        if file_name:
            # todo если ты хочешь использовать метод как статичный, то он им и должен быть
            ControllerMet.read(file_name, self.__patientse, self.__doctorse, self.__appealse)

    def print(self):
        for item in self.__doctorse, self.__patientse, self.__appealse:
            print(item)


x = Pan("data.json")
x.print()
