from menuBS import *
from calcBS import *
from maxValueBS import *
from menuEventsBS import *

menu = MenuBS(root)
calc = CalcBS()
maxValue = MaxValueBS()
menuEvents = MenuEventsBS(calc, maxValue)

btnCalc = Button(text='Kalkulator', width=18, command=lambda: menuEvents.openCalcPage())
btnMaxValue = Button(text='Większa liczba', width=24, command=lambda: menuEvents.openMaxValuePage())

menu.addElement(btnCalc)
menu.addElement(btnMaxValue)

menu.pack()
calc.pack()

messagebox.showinfo("Info", "Proszę prawidłowo wpisywać matematyczne działania i liczby!")

root.mainloop()