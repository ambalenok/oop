from controllers.Handling import Handling


class Main(object):
    def __init__(self):
        handling = Handling()
        self.__list = handling.read()

    def read(self):
        for item in self.__list:
            print(item)


x = Main()
x.read()
