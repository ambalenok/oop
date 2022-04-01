from model.Appeals import Appeals
from service.ClassListService import ClassListService


class ControllerApp(object):
    @staticmethod
    def ListApp(appeals, appealse, doctorse, patientse):
        for item in appeals:
            appeals = Appeals(item["id"], ClassListService.getByID(doctorse, item["doctors"]),
                              ClassListService.getByID(patientse, item["patients"]),
                              item["date"], item["diagnos"], item["cost"])
            appealse.append(appeals)
