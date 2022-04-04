from model.Appeals import Appeals
from service.ClassListService import ClassListService


class ControllerApp(object):

    @staticmethod
    def list(appeals, appealse, doctorse, patientse):
        for item in appeals:
            appeals = Appeals(item["id"], ClassListService.getByID(doctorse, item["doctors"]),
                              ClassListService.getByID(patientse, item["patients"]),
                              item["date"], item["diagnos"], item["cost"])
            appealse.append(appeals)

    @staticmethod
    def dict(appealse, data):
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
