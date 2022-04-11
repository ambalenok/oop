from model.Appeals import Appeals
from service.ClassListService import ClassListService


class ControllerApp(object):
    # todo не верная реализация. Тут должны быть CRUD (я их писал для примера в удалённом общем контроллере) операции
    #  и не статичными методами

    def write(self, appeals, patientse, doctorse):
        appealse = list()
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
