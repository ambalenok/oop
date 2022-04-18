from controllers.BasiController import BasiController


class Main(object):
    def __init__(self):
        basicontroller = BasiController()
        self.__list = basicontroller.read()

    def read(self):
        for item in self.__list:
            print(item)

#
x = Main()
x.read()
