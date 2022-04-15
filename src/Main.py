import configparser
from controllers.BasiController import BasiController


class Main(object):
    def __init__(self, file_name=""):
        basiController = BasiController(file_name)

        if file_name:
            self.__list = basiController.read()

    def read(self):
        for item in self.__list:
            print(item)


config = configparser.ConfigParser()
config.read("settings.conf")

x = Main(config["addr"]["root"])
x.read()
