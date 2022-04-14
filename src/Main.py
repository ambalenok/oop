from controllers.BasiController import BasiController


class Main(object):
    def __init__(self, file_name=""):
        basiController = BasiController()

        self.__list = basiController.read(file_name)

    def read(self):
        for item in self.__list:
            print(item)


x = Main("data.json")
x.read()
