#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 3 – 8.
from tkinter import *

root = Tk()
root.geometry('500x100')

def var():
    strof=num.get()
    strof.upper()
    final_0 =f"{strof}"
Label(text='Ведите текст: ').grid(row=1, column=0)
num=Entry(width='50')
num.grid(row=1,column=1,sticky='w')
Button(text='Сделать все буквы заглавными',bg='yellow',activebackground='yellow',
       command=var).grid(row=2,column=1,sticky='w')
Label(text='Результат:').grid(row=3,column=0)
final_0=Label()
final_0.grid(row=3,column=1,stick='w')
root.mainloop()