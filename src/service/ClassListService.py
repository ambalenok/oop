class ClassListService(object):

    @staticmethod
    def getByID(classlist, id):
        # todo метод не работает
        for item in classlist:
            if item.getID() == id:
                item += item
        return item
