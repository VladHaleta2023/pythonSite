from root import *
from objectPageBS import *
from additionaFunctions import *
from tkinter import messagebox

def resEventMaxValue(value1, value2, entry1, entry2):
    try:
        value1 = str(value1)
        value2 = str(value2)

        value1 = AdditionalFunctions.onlyPoint(value1)
        value2 = AdditionalFunctions.onlyPoint(value2)

        value1 = float(value1)
        value2 = float(value2)

        if value1 > value2:
            entry1['bg'] = 'green'
            entry2['bg'] = 'white'
        elif value1 == value2:
            entry1['bg'] = 'white'
            entry2['bg'] = 'white'
        else:
            entry1['bg'] = 'white'
            entry2['bg'] = 'green'
    except:
        entry1['bg'] = 'white'
        entry2['bg'] = 'white'

        messagebox.showerror("Błąd", "Proszę prawidłowo wpisywać liczby!")

class MaxValueBS(ObjectPageBS):
    __inputValue1 = StringVar()
    __inputValue2 = StringVar()

    def getValue1(self):
        return str(self.__inputValue1)

    def getValue2(self):
        return str(self.__inputValue2)

    def __init__(self, resEvent=resEventMaxValue):
        # Create main style Calculation buttons
        self.entryValue1 = Entry(root,
                          textvariable=self.__inputValue1,
                          font=('verdana', 18),
                          width=14,
                          bg='white',
                          fg='black')

        self.entryValue2 = Entry(root,
                           textvariable=self.__inputValue2,
                           font=('verdana', 18),
                           width=14,
                           bg='white',
                           fg='black')

        self.btnResult = Button(root,
                             command=lambda: resEvent(self.__inputValue1.get(),
                                                      self.__inputValue2.get(),
                                                      self.entryValue1,
                                                      self.entryValue2),
                             anchor=CENTER,
                             text='Result',
                             bg='purple',
                             fg='white',
                             font=('verdana', 24),
                             width=10,
                             cursor="hand2",
                             height=1)

    def pack(self):
        try:
            self.__init__()
            self.entryValue1.pack()
            self.entryValue1.place(x=50, y=96)
            self.entryValue2.pack()
            self.entryValue2.place(x=300, y=96)
            self.btnResult.pack()
            self.btnResult.place(x=173, y=150)
        except:
            return

    def unpack(self):
        try:
            self.entryValue1.destroy()
            self.entryValue2.destroy()
            self.btnResult.destroy()
        except:
            return