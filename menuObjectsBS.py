class MenuObjectBS:
    name = ""
    object = None

    def __init__(self, name, object):
        self.name = name
        self.object = object

class MenuObjectsBS:
    def __init__(self, listMenuObjects=[]):
        self.listMenuObjects = listMenuObjects

    def addObject(self, name, object):
        try:
            self.listMenuObjects.append(MenuObjectBS(name, object))
        except:
            return

    def removeObject(self, name):
        try:
            for i in range(0, len(self.listMenuObjects)):
                if self.listMenuObjects[i].name == str(name):
                    list(self.listMenuObjects).pop(i)
        except:
            return

    def __destroyAll(self):
        try:
            for i in range(0, len(self.listMenuObjects)):
                self.listMenuObjects[i].object.unpack()
        except:
            return

    def openObjectPage(self, nameObjectMenu):
        try:
            self.__destroyAll()
            for i in range(0, len(self.listMenuObjects)):
                if nameObjectMenu == self.listMenuObjects[i].name:
                    self.listMenuObjects[i].object.pack()
        except:
            return