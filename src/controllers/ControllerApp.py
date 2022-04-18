from controllers.BasiController import BasiController
from model.Appeals import Appeals
from service.ClassListService import ClassListService


class ControllerApp(object):

    def read(self, patientse, doctorse):
        appealse = list()
        basicontroller = BasiController()
        appeals = basicontroller.baza('app')
        for item in appeals:
            appeals = Appeals(item["id"], ClassListService.getByID(doctorse, item["doctors"]),
                              ClassListService.getByID(patientse, item["patients"]),
                              item["date"], item["diagnos"], item["cost"])
            appealse.append(appeals)
        return appealse

    def dict(self, appealse, data):
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

    def delet(self, list, id):
        for item in list:
            if item.getID() == id:
                del list[id % 100]
                return list
        else:
            return list
