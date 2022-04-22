import json
import configparser


class BaseController(object):

    def __init__(self):
        # self.id = id
        # self.surname = surname
        # self.patronymic = patronymic
        self.config = configparser.ConfigParser()
        self.config.read("settings.conf")

    def choiceList(self, item, key):
        if key == 'pat':
            return self.getModelP(item)
        if key == 'doc':
            return self.getModelD(item)


    def getDataByKey(self, key):
        file_name = self.config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]

    def read(self, valueKey):
        baseList = list()
        valueClass = self.getDataByKey(valueKey)
        for item in valueClass:
            val = self.choiceList(item, valueKey)
            baseList.append(val)
        return baseList
