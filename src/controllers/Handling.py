from controllers.ControllerDoc import ControllerDoc
from controllers.ControllerPat import ControllerPat
from controllers.ControllerApp import ControllerApp
from controllers.BasiController import BasiController

#
class Handling(BasiController):
    def read(self):
        controllerPat = ControllerPat()
        controllerDoc = ControllerDoc()
        controllerApp = ControllerApp()

        patientse = controllerPat.read()
        doctorse = controllerDoc.read()
        appealse = controllerApp.read(patientse, doctorse)
        self.__list = patientse + doctorse + appealse
        return self.__list
