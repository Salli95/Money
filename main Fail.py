from tkinter import *
from tkinter.ttk import Combobox  

def clicker():
    d

window =Tk()
window.title("Пересчет доларов")
window.geometry('500x400')

hello = Label(window, text="С какой валюты будем переводить ?" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=0)
combo = Combobox(window)
combo['values'] = ("Доллар","Тенге","Евро") 
combo.grid(column=0, row=1) 

hello = Label(window, text="В какую валюту будем переволить? ?" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=4)
secondVAL= Combobox(window)
secondVAL['values'] = ("Доллар","Тенге","Евро") 
secondVAL.grid(column=0, row=5) 

Button=Button(window,text="Посчитать ", command=clicker)
Button.grid(column=0 , row=6)

window.mainloop()