import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#00a8f3', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить работника', command=self.open_dialog, bg='#00a8f3',
                                         bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#00a8f3',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#00a8f3',
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#00a8f3',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#00a8f3',
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'name', 'second', 'sex', 'old', 'prof', 'score'),
                                 height=15, show='headings')

        self.tree.column('user_id', width=180, anchor=tk.CENTER)
        self.tree.column('name', width=100, anchor=tk.CENTER)
        self.tree.column('second', width=150, anchor=tk.CENTER)
        self.tree.column('sex', width=140, anchor=tk.CENTER)
        self.tree.column('old', width=140, anchor=tk.CENTER)
        self.tree.column('prof', width=180, anchor=tk.CENTER)
        self.tree.column('score', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='Фамилия')
        self.tree.heading('name', text='Имя')
        self.tree.heading('second', text='Отчество')
        self.tree.heading('sex', text='Пол')
        self.tree.heading('old', text='Возраст')
        self.tree.heading('prof', text='Профессия')
        self.tree.heading('score', text='Стаж работы')

        self.tree.pack()

    def records(self, user_id, name, second, sex, old, prof, score):
        self.db.insert_data(user_id, name, second, sex, old, prof, score)
        self.view_records()

    def update_record(self, user_id, name, second, sex, old, prof, score):
        self.db.cur.execute("""UPDATE БЮРО_ПО_ТРУДОЙСТРОЙСТВУ SET user_id=?, name=?, second=?, sex=?, 
        old=?,prof=?, score=?
        WHERE user_id=?""",
                            (user_id, name, second, sex, old, prof, score, self.tree.set(self.tree.selection()[0],
                                                                                         '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM БЮРО_ПО_ТРУДОЙСТРОЙСТВУ""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end',values=row) for row in self.db.cur.fetchall()]


    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM БЮРО_ПО_ТРУДОЙСТРОЙСТВУ WHERE user_id=?""",
                                (self.tree.set(selection_item, '#1'),(self.tree.insert(self.db.cur.fetchall()))))
        self.db.con.commit()
        self.view_records()

    def search_records(self, score):
        score = (score,)
        self.db.cur.execute("""SELECT * FROM БЮРО_ПО_ТРУДОЙСТРОЙСТВУ WHERE score>=?""",score)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x320+400+600')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Фамилия')
        label_description.place(x=30, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_name = tk.Label(self, text='Имя')
        label_name.place(x=30, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_second = tk.Label(self, text='Отчество')
        label_second.place(x=30, y=75)
        self.entry_second = ttk.Entry(self)
        self.entry_second.place(x=110, y=75)

        label_sex = tk.Label(self, text='Пол')
        label_sex.place(x=30, y=100)
        self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
        self.combobox.current(0)
        self.combobox.place(x=110, y=100)

        label_old = tk.Label(self, text='Возраст')
        label_old.place(x=30, y=125)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=125)

        label_prof = tk.Label(self, text='Профессия')
        label_prof.place(x=30, y=150)
        self.entry_prof = ttk.Entry(self)
        self.entry_prof.place(x=110, y=150)

        label_score = tk.Label(self, text='Стаж работы')
        label_score.place(x=30, y=175)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=220)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=220)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_second.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_prof.get(),
                                                                       self.entry_score.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=220)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_second.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_prof.get(),
                                                                       self.entry_score.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск по стажу работы")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):

        with sq.connect('BD/Buro.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS БЮРО_ПО_ТРУДОЙСТРОЙСТВУ (
                user_id TEXT NOT NULL,
                name TEXT NOT NULL,
                second TEXT NOT NULL,
                sex INTEGER NOT NULL DEFAULT 1,
                old INTEGER,
                prof TEXT NOT NULL,
                score INTEGER
                )""")

    def insert_data(self, user_id, name, second, sex, old, prof, score):
        self.cur.execute("""INSERT INTO БЮРО_ПО_ТРУДОЙСТРОЙСТВУ (user_id, name, second, sex, old, prof, score) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (user_id, name, second, sex, old, prof, score))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работник")
    root.geometry("1032x450+300+200")
    root.resizable(False, False)
    root.mainloop()