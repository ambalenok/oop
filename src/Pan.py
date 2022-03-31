from controllers.ControllerMet import ControllerMet


class Pan(object):
    def __init__(self, file_name=""):
        self.__patientse = list()
        self.__doctorse = list()
        self.__appealse = list()
        if file_name:
            ControllerMet.read(file_name, self.__patientse, self.__doctorse, self.__appealse)

    def print(self):
        for item in self.__doctorse, self.__patientse, self.__appealse:
            print(item)


x = Pan("data.json")
x.print()
