from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp


class Main(object):
    def __init__(self):
        controllerPat = ControllerPat()
        controllerDoc = ControllerDoc()
        controllerApp = ControllerApp()

        patientse = controllerPat.read()
        doctorse = controllerDoc.read()
        appealse = controllerApp.read(patientse, doctorse)

        self.__list = patientse + doctorse + appealse

    def read(self):
        for item in self.__list:
            print(item)

#
x = Main()
x.read()
