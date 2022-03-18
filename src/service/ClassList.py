# todo нет смысла в этом классе. Лучше сделать его сервисным классом со статическим методом получения по ID
class ClassList(list):
    def getByID(self, id):
        for item in self:
            if item.getID() == id:
                return item
        return None
