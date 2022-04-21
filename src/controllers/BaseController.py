import json
import configparser


class BaseController(object):

    def __init__(self, id, surname, patronymic):
        self.id = id
        self.surname = surname
        self.patronymic = patronymic
        self.config = configparser.ConfigParser()
        self.config.read("settings.conf")

    def getModel(self, item, baseClass):
        valueAll = baseClass(item["id"], item["surname"], item["patronymic"], item["year"])
        return valueAll

    def getDataByKey(self, key):
        file_name = self.config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]

    def read2(self, valueKey, baseClass):
        baseList = list()
        for item in valueKey:
            valueKey = self.getModel(item)
            baseList.append(valueKey)

        return baseList
