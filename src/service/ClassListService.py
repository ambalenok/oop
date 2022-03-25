class ClassListService(list):
    def getByID(self, id):
        for item in self:
            if item.getID() == id:
                return item
        return None
