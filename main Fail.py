from tkinter import *
from tkinter.ttk import Combobox  
from парсингн import Valut

def convert_currency():
    amount = float(txt.get())
    from_currency = (firstVAL.get())
    to_currency = (secondVAL.get())
    # print(float(Valut[from_currency]))
    # print(float(Valut[to_currency]))
    if from_currency in Valut and to_currency in Valut:
       
        amount_in_usd = amount / float(Valut[from_currency])
        result = amount_in_usd * float(Valut[to_currency])
        
        label.config(text=f"{amount} {from_currency} is equivalent to {result:.2f} {to_currency}")

    else:
        label.config(text="Unknown currency")
      
window = Tk()
window.title("Пересчет доларов")
window.geometry('500x400')

hello = Label(window, text="С какой валюты будем переводить ?", font=("Arial bold", 20))
hello.grid(column=0, row=0)
firstVAL = Combobox(window)
firstVAL['values'] = ("USD", "Kazakhstani Tenge", "Euro", "Russian Ruble") 
firstVAL.grid(column=0, row=1) 

hello = Label(window, text="В какую валюту будем переводить ?", font=("Arial bold", 20))
hello.grid(column=0, row=4)
secondVAL = Combobox(window)
secondVAL['values'] =("USD", "Kazakhstani Tenge", "Euro", "Russian Ruble") 
secondVAL.grid(column=0, row=5) 

hello = Label(window, text="Введите сумму", font=("Arial bold", 20))
hello.grid(column=0, row=6)

txt = Entry(window, width=10)
txt.focus()
txt.grid(column=0, row=7)

Button = Button(window, text="Посчитать", command=convert_currency)
Button.grid(column=0, row=8)

label = Label(window, text="")
label.grid(column=0, row=9)

window.mainloop()
