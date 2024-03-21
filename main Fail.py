from tkinter import *
from tkinter.ttk import Combobox  

def clicker():
    d

window =Tk()
window.title("Пересчет доларов")
window.geometry('500x400')

hello = Label(window, text="С какой валюты будем переводить ?" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=0)
firstVAL = Combobox(window)
firstVAL['values'] = ("Доллар","Тенге","Евро") 
firstVAL.grid(column=0, row=1) 

hello = Label(window, text="В какую валюту будем переволить ?" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=4)
secondVAL= Combobox(window)
secondVAL['values'] = ("Доллар","Тенге","Евро") 
secondVAL.grid(column=0, row=5) 

hello = Label(window, text="Введите сумму" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=6)

txt=Entry(window,width=10)
txt.focus()
txt.grid(column=0,row=7)

Button=Button(window,text="Посчитать ", command=clicker)
Button.grid(column=0 , row=8)

window.mainloop()