from tkinter import *
from tkinter.ttk import Combobox  
from парсингн import Valut

def clicker():
    comboFERST=firstVAL.get()
    comboSECOND=secondVAL.get()
    sam=txt.get()
    Tenge=Valut["Kazakhstani Tenge"]
    
    if comboFERST == "Доллар" and comboSECOND=="Тенге":
     Dollar=int(sam)/float(Tenge)
     label.config(text=Dollar)
     print(Dollar)
    else:
        print("Ошибка")
        label.config(text="Ошибка")
     
    # print("первый:",comboFERST)
    # print("второй:",comboSECOND)
    # print("сумма :",sam)
        
window =Tk()
window.title("Пересчет доларов")
window.geometry('500x400')

hello = Label(window, text="С какой валюты будем переводить ?" ,font = ("Arial bold",18))
hello.grid(column=0 ,row=0)
firstVAL = Combobox(window)
firstVAL['values'] = ("Доллар","Тенге","Евро","Рубль") 
firstVAL.grid(column=0, row=1) 

hello = Label(window, text="В какую валюту будем переволить ?" ,font = ("Arial bold",18))
hello.grid(column=0 ,row=4)
secondVAL= Combobox(window)
secondVAL['values'] = ("Доллар","Тенге","Евро","Рубль") 
secondVAL.grid(column=0, row=5) 

hello = Label(window, text="Введите сумму" ,font = ("Arial bold",20))
hello.grid(column=0 ,row=6)

txt=Entry(window,width=10)
txt.focus()
txt.grid(column=0,row=7)

Button=Button(window,text="Посчитать ", command=clicker)
Button.grid(column=0 , row=8)

label = Label(text="//////////")
label.grid(column=0 , row=9)

window.mainloop()
