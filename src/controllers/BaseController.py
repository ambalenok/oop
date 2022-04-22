import json
import configparser


class BaseController(object):

    def __init__(self):
        # self.id = id
        # self.surname = surname
        # self.patronymic = patronymic
        self.config = configparser.ConfigParser()
        self.config.read("settings.conf")

    def getJopa(self,item, baseClass, key):
        if key == 'pat':
            jojo2 = self.getModelP(item)
        else:
            jojo2 = self.getModelD(item)

        jojo = (baseClass(item["id"], item["surname"], item["patronymic"], jojo2))

        return jojo


    def getDataByKey(self, key):
        file_name = self.config["addr"]["root"]
        with open(file_name) as file_input:
            data: dict = json.load(file_input)
            chek = {'pat': data.get("patients"), 'doc': data.get("doctors"), 'app': data["appeals"]}
        return chek[key]

    def read(self, valueKey, baseClass):
        key = valueKey
        baseList = list()
        valueKey = self.getDataByKey(valueKey)
        for item in valueKey:
            val = self.getJopa(item, baseClass, key)
            baseList.append(val)
        return baseList
