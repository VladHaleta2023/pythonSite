from root import *
from objectPageBS import *
from tkinter import ttk
from resultBS import *

# Calculation class
class CalcBS(ObjectPageBS):
    # Elements for buttons
    __inputStr = StringVar()
    inputStr = __inputStr
    __inDegrees = StringVar()
    __decimalPlaces = StringVar()

    def __resCalculation(self):
        try:
            inputStr = str(self.__inputStr.get())
            inDegress = str(self.__inDegrees.get())
            decimalPlaces = str(self.__decimalPlaces.get())

            if inDegress == "Tak":
                inDegress = True
            else:
                inDegress = False

            if decimalPlaces == "":
                decimalPlaces = None
            else:
                decimalPlaces = int(decimalPlaces)

            r = ResultBS(inputStr, inDegress, decimalPlaces)
            self.__inputStr.set(r.getResult())
        except:
            self.__inputStr.set("")

    def __getValue(self, value):
        self.__inputStr.set(self.__insert(self.entry.index(INSERT), str(value)))
        self.__changeCursorEntry()

    def __getSigns(self, sign):
        self.__inputStr.set(self.__insert(self.entry.index(INSERT), sign))
        self.__changeCursorEntry()

    def __getFunc(self, func, nextPos=5):
        self.__inputStr.set(self.__insert(self.entry.index(INSERT), func))
        self.__changeCursorEntry(nextPos)

    def __insert(self, index, insertStr):
        try:
            return self.__inputStr.get()[:index] + str(insertStr) + self.__inputStr.get()[index:]
        except:
            return

    def __delete(self, index):
        try:
            self.__changeCursorEntry(-1)
            return self.__inputStr.get()[:index - 1] + self.__inputStr.get()[index:]
        except:
            return

    def __changeCursorEntry(self, value=1):
        self.entry.icursor(self.entry.index(INSERT) + value)

    def _Sinus(self):
        self.__getFunc("sin()")

    def _Cosinos(self):
        self.__getFunc("cos()")

    def _Exp(self):
        self.__getFunc("exp()")

    def _Sqrt(self):
        self.__getFunc("sqrt()", 6)

    def _Zero(self):
        self.__getValue(0)

    def _One(self):
        self.__getValue(1)

    def _Two(self):
        self.__getValue(2)

    def _Three(self):
        self.__getValue(3)

    def _Four(self):
        self.__getValue(4)

    def _Five(self):
        self.__getValue(5)

    def _Six(self):
        self.__getValue(6)

    def _Seven(self):
        self.__getValue(7)

    def _Eight(self):
        self.__getValue(8)

    def _Nine(self):
        self.__getValue(9)

    def _Plus(self):
        self.__getSigns('+')

    def _Minus(self):
        self.__getSigns('-')

    def _Division(self):
        self.__getSigns('/')

    def _Multiply(self):
        self.__getSigns('*')

    def _Pow(self):
        self.__getSigns('^')

    def _Point(self):
        self.__getSigns('.')

    def _LB(self):
        self.__getSigns('(')

    def _RB(self):
        self.__getSigns(')')

    def _Delete(self):
        self.__inputStr.set(self.__delete(self.entry.index(INSERT)))

    def _Clear(self):
        self.__inputStr.set("")

    def __init__(self):
        # Create main style Calculation buttons
        self.entry = Entry(root,
                          textvariable=self.__inputStr,
                          font=('verdana', 18),
                          width=48,
                          bg='white',
                          fg='black')
        self.btnSin = Button(root,
                            command=self._Sinus,
                            anchor=CENTER,
                            text='sin',
                            bg='#6A5ACD',
                            fg='white',
                            font=('verdana', 24),
                            width=6,
                            cursor="hand2",
                            height=1)
        self.btnCos = Button(root,
                            command=self._Cosinos,
                            anchor=CENTER,
                            text='cos',
                            bg='#6A5ACD',
                            fg='white',
                            font=('verdana', 24),
                            width=6,
                            cursor="hand2",
                            height=1)
        self.btnExp = Button(root,
                        anchor=CENTER,
                        command=self._Exp,
                        text='exp',
                        bg='#6A5ACD',
                        fg='white',
                        font=('verdana', 24),
                        width=6,
                        cursor="hand2",
                        height=1)
        self.btnSqrt = Button(root,
                         command=self._Sqrt,
                         anchor=CENTER,
                         text='sqrt',
                         bg='#6A5ACD',
                         fg='white',
                         font=('verdana', 24),
                         width=6,
                         cursor="hand2",
                         height=1)
        self.btnDelete = Button(root,
                           command=self._Delete,
                           anchor=CENTER,
                           text='Delete',
                           bg='purple',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnOne = Button(root,
                             command=self._Seven,
                            text='7',
                            anchor=CENTER,
                            bg='#6A5ACD',
                            fg='white',
                            font=('verdana', 24),
                            width=6,
                            cursor="hand2",
                            height=1)
        self.btnTwo = Button(root,
                             command=self._Eight,
                        text='8',
                        anchor=CENTER,
                        bg='#6A5ACD',
                        fg='white',
                        font=('verdana', 24),
                        width=6,
                        cursor="hand2",
                        height=1)
        self.btnThree = Button(root,
                               command=self._Nine,
                        text='9',
                        anchor=CENTER,
                        bg='#6A5ACD',
                        fg='white',
                        font=('verdana', 24),
                        width=6,
                        cursor="hand2",
                        height=1)
        self.btnPlus = Button(root,
                              command=self._Plus,
                        text='+',
                        anchor=CENTER,
                        bg='#6A5ACD',
                        fg='white',
                        font=('verdana', 24),
                        width=6,
                        cursor="hand2",
                        height=1)
        self.btnMinus = Button(root,
                               command=self._Minus,
                        text='-',
                        anchor=CENTER,
                        bg='#6A5ACD',
                        fg='white',
                        font=('verdana', 24),
                        width=6,
                        cursor="hand2",
                        height=1)
        self.btnFour = Button(root,
                              command=self._Four,
                        text='4',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnFive = Button(root,
                              command=self._Five,
                        text='5',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnSix = Button(root,
                             command=self._Six,
                        text='6',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnMultiply = Button(root,
                                  command=self._Multiply,
                            text='*',
                            anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnDivision = Button(root,
                                  command=self._Division,
                        text='/',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnSeven = Button(root,
                               command=self._One,
                        text='1',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnEight = Button(root,
                               command=self._Two,
                        text='2',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnNine = Button(root,
                              command=self._Three,
                        text='3',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnPoint = Button(root,
                               command=self._Point,
                        text='.',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)
        self.btnPow = Button(root,
                             command=self._Pow,
                        text='^',
                        anchor=CENTER,
                           bg='#6A5ACD',
                           fg='white',
                           font=('verdana', 24),
                           width=6,
                           cursor="hand2",
                           height=1)

        self.btnZero = Button(root,
                             command=self._Zero,
                             text='0',
                             anchor=CENTER,
                             bg='#6A5ACD',
                             fg='white',
                             font=('verdana', 24),
                             width=6,
                             cursor="hand2",
                             height=1)

        self.btnClear = Button(root,
                              command=self._Clear,
                              text='Clear',
                              anchor=CENTER,
                              bg='red',
                              fg='white',
                              font=('verdana', 24),
                              width=13,
                              padx=5,
                              cursor="hand2",
                              height=1)

        self.btnLeftBracket = Button(root,
                             command=self._LB,
                             text='(',
                             anchor=CENTER,
                             bg='#6A5ACD',
                             fg='white',
                             font=('verdana', 24),
                             width=6,
                             cursor="hand2",
                             height=1)

        self.btnRightBracket = Button(root,
                             command=self._RB,
                             text=')',
                             anchor=CENTER,
                             bg='#6A5ACD',
                             fg='white',
                             font=('verdana', 24),
                             width=6,
                             cursor="hand2",
                             height=1)

        self.btnResult = Button(root,
                            command=self.__resCalculation,
                            anchor=CENTER,
                            text='Result',
                            bg='green',
                            fg='white',
                            font=('verdana', 24),
                            width=36,
                            cursor="hand2",
                            height=1)

        self.lblInDegrees = Label(root,
                                  anchor=CENTER,
                                  text='In Degress:',
                                  fg='white',
                                  bg='#18171C',
                                  font=('verdana', 18))

        self.comboBox = ttk.Combobox(root,
                                     width=4,
                                     textvariable=self.__inDegrees,
                                     font=('verdana', 18))
        self.comboBox['values'] = (
            'Tak',
            'Nie')
        self.comboBox.current(1)

        self.lblDecimalPlaces = Label(root,
                                  anchor=CENTER,
                                  text='Decimal places:',
                                  fg='white',
                                  bg='#18171C',
                                  font=('verdana', 18))

        self.entryDecimalPlaces = Entry(root,
                                        textvariable=self.__decimalPlaces,
                                        font=('verdana', 18),
                                        width=10,
                                        bg='white',
                                        fg='black')

    def pack(self):
        try:
            self.__init__()
            self.entry.pack()
            self.entry.place(x=0, y=96)
            self.btnSin.pack(anchor=NW, side=LEFT)
            self.btnSin.place(x=0, y=160)
            self.btnCos.pack(anchor=NW, side=LEFT)
            self.btnCos.place(x=150, y=160)
            self.btnExp.pack(anchor=NW, side=LEFT)
            self.btnExp.place(x=300, y=160)
            self.btnSqrt.pack(anchor=NW, side=LEFT)
            self.btnSqrt.place(x=450, y=160)
            self.btnDelete.pack(anchor=NW, side=LEFT)
            self.btnDelete.place(x=600, y=160)
            self.btnTwo.pack(anchor=NW, side=LEFT)
            self.btnTwo.place(x=150, y=248)
            self.btnOne.pack(anchor=NW, side=LEFT)
            self.btnOne.place(x=0, y=248)
            self.btnThree.pack(anchor=NW, side=LEFT)
            self.btnThree.place(x=300, y=248)
            self.btnPlus.pack(anchor=NW, side=LEFT)
            self.btnPlus.place(x=450, y=248)
            self.btnMinus.pack(anchor=NW, side=LEFT)
            self.btnMinus.place(x=600, y=248)
            self.btnFour.pack(anchor=NW, side=LEFT)
            self.btnFour.place(x=0, y=336)
            self.btnFive.pack(anchor=NW, side=LEFT)
            self.btnFive.place(x=150, y=336)
            self.btnSix.pack(anchor=NW, side=LEFT)
            self.btnSix.place(x=300, y=336)
            self.btnMultiply.pack(anchor=NW, side=LEFT)
            self.btnMultiply.place(x=450, y=336)
            self.btnDivision.pack(anchor=NW, side=LEFT)
            self.btnDivision.place(x=600, y=336)
            self.btnSeven.pack(anchor=NW, side=LEFT)
            self.btnSeven.place(x=0, y=424)
            self.btnEight.pack(anchor=NW, side=LEFT)
            self.btnEight.place(x=150, y=424)
            self.btnNine.pack(anchor=NW, side=LEFT)
            self.btnNine.place(x=300, y=424)
            self.btnPoint.pack(anchor=NW, side=LEFT)
            self.btnPoint.place(x=450, y=424)
            self.btnPow.pack(anchor=NW, side=LEFT)
            self.btnPow.place(x=600, y=424)
            self.btnZero.pack(anchor=NW, side=LEFT)
            self.btnZero.place(x=150, y=512)
            self.btnLeftBracket.pack(anchor=NW, side=LEFT)
            self.btnLeftBracket.place(x=0, y=512)
            self.btnRightBracket.pack(anchor=NW, side=LEFT)
            self.btnRightBracket.place(x=300, y=512)
            self.btnClear.pack(anchor=NW, side=LEFT)
            self.btnClear.place(x=450, y=512)
            self.btnResult.pack(anchor=NW, side=LEFT)
            self.btnResult.place(x=0, y=600)
            self.lblInDegrees.pack(anchor=NW, side=LEFT)
            self.lblInDegrees.place(x=20, y=700)
            self.comboBox.pack(anchor=NW, side=LEFT)
            self.comboBox.place(x=180, y=700)
            self.lblDecimalPlaces.pack(anchor=NW, side=LEFT)
            self.lblDecimalPlaces.place(x=300, y=700)
            self.entryDecimalPlaces.pack(anchor=NW, side=LEFT)
            self.entryDecimalPlaces.place(x=500, y=700)
        except:
            return


    def unpack(self):
        try:
            self.entry.destroy()
            self.btnSin.destroy()
            self.btnCos.destroy()
            self.btnExp.destroy()
            self.btnSqrt.destroy()
            self.btnDelete.destroy()
            self.btnTwo.destroy()
            self.btnOne.destroy()
            self.btnThree.destroy()
            self.btnPlus.destroy()
            self.btnMinus.destroy()
            self.btnFour.destroy()
            self.btnFive.destroy()
            self.btnSix.destroy()
            self.btnMultiply.destroy()
            self.btnDivision.destroy()
            self.btnSeven.destroy()
            self.btnEight.destroy()
            self.btnNine.destroy()
            self.btnPoint.destroy()
            self.btnPow.destroy()
            self.btnZero.destroy()
            self.btnResult.destroy()
            self.lblInDegrees.destroy()
            self.lblDecimalPlaces.destroy()
            self.entryDecimalPlaces.destroy()
            self.comboBox.destroy()
            self.btnLeftBracket.destroy()
            self.btnRightBracket.destroy()
            self.btnClear.destroy()
        except:
            return