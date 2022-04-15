from controllers.BasiController import BasiController


class Main(object):
    def __init__(self, file_name=""):
        basiController = BasiController(file_name)

        if file_name:
            self.__list = basiController.read()

    def read(self):
        for item in self.__list:
            print(item)


x = Main("data.json")
x.read()
