class ClassListService(object):
    # todo переименуй self на более понятное название.
    # todo Следи за названиями переменных. По их названию должно быть понятно, что в них находиться
    @staticmethod
    def getByID(self, id):
        # todo цикл работает не корректно, сейчас он проверяет только первый элемент в списке и дальше не идёт
        # todo разберись почему и исправь ошибку
        for item in self:
            if item.getID() == id:
                return item
            return None
