class ClassListService(object):

    @staticmethod
    def getByID(classlist, id):
        # todo цикл работает не корректно, сейчас он проверяет только первый элемент в списке и дальше не идёт
        # todo разберись почему и исправь ошибку

        while len(classlist):
            for item in classlist:
                if item.getID() == id:
                    return item
                return None
