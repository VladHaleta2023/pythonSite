import math
from additionaFunctions import *
from tkinter import messagebox

class ResultBS:
    # Start and end index of brackets
    __start = __end = 0
    __values = []
    __signs = []
    # String type functions
    __func = ""
    # Check if is error
    __error = False
    __inDegrees = False
    __decimalPlaces = None

    def __init__(self, inputStr, inDegress = False, decimalPlaces = None):
        self.inputStr = inputStr
        self.__inDegrees = inDegress
        self.__decimalPlaces = decimalPlaces

    def __findBrackets(self, inputStr):
        try:
            self.__start = self.__end = 0
            for i in range(1, len(inputStr) + 1):
                if inputStr[len(inputStr) - i] == '(':
                    self.__start = len(inputStr) - i
                    break

            if (inputStr[self.__start - 1] == 'n' and
                inputStr[self.__start - 2] == 'i' and
                inputStr[self.__start - 3] == 's'):
                self.__func = "sin"
            elif (inputStr[self.__start - 1] == 's' and
                inputStr[self.__start - 2] == 'o' and
                inputStr[self.__start - 3] == 'c'):
                self.__func = "cos"
            elif (inputStr[self.__start - 1] == 'p' and
                inputStr[self.__start - 2] == 'x' and
                inputStr[self.__start - 3] == 'e'):
                self.__func = "exp"
            elif (inputStr[self.__start - 1] == 't' and
                inputStr[self.__start - 2] == 'r' and
                inputStr[self.__start - 3] == 'q' and
                inputStr[self.__start - 4] == 's'):
                self.__func = "sqrt"

            for i in range(self.__start + 1, len(inputStr)):
                if inputStr[i] == ')':
                    self.__end = i
                    break
        except:
            self.__error = True

    def __useFunc(self, valueStr, inputStr):
        if self.__func == "sin":
            if self.__inDegrees == True:
                valueStr = math.sin(math.radians(valueStr))
            else:
                valueStr = math.sin(valueStr)
            if valueStr < 0:
                valueStr = list(str(valueStr))
                valueStr[0] = '~'
                valueStr = self.__listToStr(valueStr)

            inputStr = inputStr[:self.__start - 3] + str(valueStr) + inputStr[self.__end + 1:]
        elif self.__func == "cos":
            if self.__inDegrees == True:
                valueStr = math.cos(math.radians(valueStr))
            else:
                valueStr = math.cos(valueStr)
            if valueStr < 0:
                valueStr = list(str(valueStr))
                valueStr[0] = '~'
                valueStr = self.__listToStr(valueStr)

            inputStr = inputStr[:self.__start - 3] + str(valueStr) + inputStr[self.__end + 1:]
        elif self.__func == "exp":
            valueStr = math.exp(valueStr)
            if valueStr < 0:
                valueStr = list(str(valueStr))
                valueStr[0] = '~'
                valueStr = self.__listToStr(valueStr)

            inputStr = inputStr[:self.__start - 3] + str(valueStr) + inputStr[self.__end + 1:]
        elif self.__func == "sqrt":
            valueStr = math.sqrt(valueStr)
            if valueStr < 0:
                valueStr = list(str(valueStr))
                valueStr[0] = '~'
                valueStr = self.__listToStr(valueStr)

            inputStr = inputStr[:self.__start - 4] + str(valueStr) + inputStr[self.__end + 1:]
        else:
            self.__error = True
        self.__func = ""
        return inputStr

    def __onlyOnePlusAndMinus(self, valueStr):
        try:
            resValue = ""
            valueStr = list(valueStr)
            for i in range(0, len(valueStr)):
                if ((valueStr[i] == '+' or valueStr[i] == '-') and
                    (valueStr[i + 1] == '+' or valueStr[i + 1] == '-')):
                    if valueStr[i] == '+':
                        if valueStr[i + 1] == '+':
                            valueStr[i] = ''
                            valueStr[i + 1] = '+'
                        elif valueStr[i + 1] == '-':
                            valueStr[i] = ''
                            valueStr[i + 1] = '-'
                    if valueStr[i] == '-':
                        if valueStr[i + 1] == '+':
                            valueStr[i] = ''
                            valueStr[i + 1] = '-'
                        elif valueStr[i + 1] == '-':
                            valueStr[i] = ''
                            valueStr[i + 1] = '+'
                resValue += str(valueStr[i])
            return resValue
        except:
            return self.__error

    def __Pow(self):
        try:
            usePow = True
            while(usePow):
                usePow = False
                for i in range(0, len(self.__signs)):
                    if self.__signs[i] == "^":
                        self.__values[i - 1] = self.__values[i - 1] ** self.__values[i]
                        self.__values.pop(i)
                        self.__signs.pop(i)
                        usePow = True
                        break
        except:
            self.__error = True

    def __MD(self):
        try:
            useMD = True
            while (useMD):
                useMD = False
                for i in range(0, len(self.__signs)):
                    if self.__signs[i] == "*":
                        self.__values[i - 1] = self.__values[i - 1] * self.__values[i]
                        self.__values.pop(i)
                        self.__signs.pop(i)
                        useMD = True
                        break
                    elif self.__signs[i] == "/":
                        self.__values[i - 1] = self.__values[i - 1] / self.__values[i]
                        self.__values.pop(i)
                        self.__signs.pop(i)
                        useMD = True
                        break
        except:
            self.__error = True

    def __PM(self):
        result = 0
        try:
            for i in range(0, len(self.__signs)):
                if self.__signs[i] == "+":
                    result += self.__values[i]
                elif self.__signs[i] == "-":
                    result -= self.__values[i]
        except:
            self.__error = True

        return result

    def __firstSymbolMustBeSign(self, valueStr):
        try:
            if (valueStr[0] != "+" and
                valueStr[0] != "-" and
                valueStr[0] != "*" and
                valueStr[0] != "/" and
                valueStr[0] != "^"):
                self.__signs.append("+")
        except:
            self.__error = True

    def __createMathMatrix(self, valueStr):
        minus = 1
        value = ""

        try:
            for i in range(0, len(list(valueStr))):
                if (valueStr[i] == "-" and minus == -1 and
                    (valueStr[i - 1] == "*" or
                    valueStr[i - 1] == "/" or
                    valueStr[i - 1] == "^")):
                    continue
                if (valueStr[i] == "+" or
                    valueStr[i] == "*" or
                    valueStr[i] == "/" or
                    valueStr[i] == "^" or
                    valueStr[i] == "-"):

                    self.__signs.append(valueStr[i])
                    try:
                        if value != "":
                            self.__values.append(float(value) * minus)
                    except:
                        return 0

                    value = ""

                    if ((valueStr[i] == "*" or
                         valueStr[i] == "/" or
                         valueStr[i] == "^") and
                            valueStr[i + 1] == "-"):
                        minus = -1
                    else:
                        minus = 1
                else:
                    if (valueStr[i] != "+" and
                        valueStr[i] != "*" and
                        valueStr[i] != "/" and
                        valueStr[i] != "^" and
                        valueStr[i] != "-"):
                        if valueStr[i] == "~":
                            value += '-'
                        else:
                            value += valueStr[i]

            self.__values.append(float(value) * minus)
        except:
            self.__error = True

    def __listToStr(self, list):
        result = ""
        for i in range(0, len(list)):
            result += str(list[i])
        return result

    def getResult(self):
        self.__signs = []
        self.__values = []

        # Copy element
        inputStr = self.inputStr
        # Static other function
        inputStr = AdditionalFunctions.onlyPoint(inputStr)

        # Delete =
        if inputStr[len(inputStr) - 1] == "=":
            inputStr = inputStr.replace("=", "")

        if inputStr == "error":
            return

        while(not self.__error):
            try:
                # Try to get value
                inputStr = float(inputStr)

                if self.__decimalPlaces == None:
                    return inputStr
                else:
                    try:
                        return round(inputStr, self.__decimalPlaces)
                    except:
                        return float(inputStr)
            except:
                try:
                    # Find brackets
                    self.__findBrackets(inputStr)

                    # If not found brackets
                    if self.__start == self.__end == 0:
                        valueStr = inputStr
                    else:
                        valueStr = str(inputStr[self.__start + 1: self.__end])

                    # Clear additional signs
                    valueStr = self.__onlyOnePlusAndMinus(valueStr)
                    # Move to list
                    valueStr = list(valueStr)

                    # Helper to divide values and signs
                    self.__firstSymbolMustBeSign(valueStr)
                    # Create matrix values and signs
                    self.__createMathMatrix(valueStr)
                    # Do Pow
                    self.__Pow()
                    # Do multiply and division
                    self.__MD()
                    # Do plus and minus and try to get float value
                    valueStr = float(self.__PM())

                    # Check Availability Sin, Cos, Exp, Sqrt
                    if self.__func != "":
                        inputStr = self.__useFunc(valueStr, inputStr)
                    else:
                        if self.__start == self.__end == 0:
                            inputStr = valueStr
                        else:
                            if valueStr < 0:
                                valueStr = list(str(valueStr))
                                # Minus is values part
                                valueStr[0] = '~'
                                valueStr = self.__listToStr(valueStr)

                            # Insert result to input String
                            insertInputStr = ""
                            for i in range(0, self.__start):
                                insertInputStr += inputStr[i]

                            insertInputStr += str(valueStr)

                            for i in range(self.__end + 1, len(inputStr)):
                                insertInputStr += inputStr[i]

                            inputStr = insertInputStr

                    # Clear lists
                    self.__signs = []
                    self.__values = []
                except:
                    # When don't get float value, then get empty
                    return ""
        # When don't get float value, then get empty
        return ""