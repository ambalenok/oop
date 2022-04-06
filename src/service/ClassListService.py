class ClassListService(object):

    @staticmethod
    def getByID(classlist, id):

        for item in classlist:
            if item.getID() == id:
                item += item
        return item
