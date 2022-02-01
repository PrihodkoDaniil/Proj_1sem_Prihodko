#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 3 – 8.
#Была выбрана задача 7_1
#Условие:
#Преобразовать в строке все строчные буквы(как латинские, так и русские) в прописные.
from tkinter import *



def var(vod):
    te['text'] = 'Измененная строка: ',num.get().upper()


root = Tk()
root.title('Преобразование всех строчных букв в прописные')
root.geometry('500x100')
Label(text='Ведите текст: ').grid(row=1, column=0)
num=Entry(width='50')
num.grid(row=1,column=1)
button1 = Button(text='Сделать все буквы заглавными',bg='yellow',activebackground='yellow')
button1.grid(row=2,column=1)
Label(text='Результат:').grid(row=3,column=0)
te=Label(font='arial 12')
te.grid(row=3,column=1)
button1.bind('<Button-1>',var)
root.mainloop()