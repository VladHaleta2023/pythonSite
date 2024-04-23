class AdditionalFunctions:
    def __init__(self):
        pass

    @staticmethod
    def onlyPoint(inputStr):
        try:
            listStr = list(inputStr)
            for i in range(0, len(listStr)):
                if listStr[i] == ',':
                    listStr[i] = '.'
            inputStr = ""
            for i in range(0, len(listStr)):
                inputStr += str(listStr[i])

            return inputStr
        except:
            return "error"