class ClassListService(object):
    @staticmethod
    def getByID(self, id):
        for item in self:
            if item.getID() == id:
                return item
            return None
