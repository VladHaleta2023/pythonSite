from menuObjectsBS import *

class MenuEventsBS:
    menuObjects = MenuObjectsBS()

    def __init__(self, calc, maxValue):
        self.calc = calc
        self.maxValue = maxValue
        self.menuObjects.addObject("calc", calc)
        self.menuObjects.addObject("maxValue", maxValue)

    def openCalcPage(self):
        self.menuObjects.openObjectPage("calc")

    def openMaxValuePage(self):
        self.menuObjects.openObjectPage("maxValue")