import tkinter as tk
from random import randint, choice
from tkinter import messagebox

main = tk.Tk()

def AddIdea ():
    value = iget.get()
    if value != '':
        with open('How.txt', '+a', encoding='utf-8') as file:
            file.write(value + '\n')
        iget.delete(0, 'end')
        tk.messagebox.showinfo('Message', ('Успешно добавлен в список'))
    else:
        tk.messagebox.showinfo('Warning', ("Не удалось добавить в список! Проверьте правильность заполнения поля и повторите попытку."))


def Randi():
     with open('How.txt', 'r', encoding='utf-8') as file:
         lines = file.readlines()
         tk.messagebox.showinfo('Generation Result', (choice(lines)))

import webbrowser
def callback(url):
    webbrowser.open_new(url)

link1 = tk.Label(main, text="Перейти на канал разработчика", font=(18), fg="blue", cursor="hand2")
link1.place(x=370, y=0)
link1.bind("<Button-1>", lambda e: callback("www.youtube.com/@laser_creative"))
link2 = tk.Label(main, text="Перейти в Telegram канал", font=(18), fg="blue", cursor="hand2")
link2.place(x=370, y=50)
link2.bind("<Button-1>", lambda e: callback("https://t.me/laser_creative"))

main.resizable(False, False)
main.title('v1.2                                                                    Генератор идей - Free Access')
main.geometry('720x360')
main['bg'] = '#E0E0E0'

idea = tk.Label(main, text='Добавьте свою идею', font= (18), fg='black', bg='#E0E0E0')
idea.place(x=30, y=80)

iget = tk.Entry(font='13', fg='black', width='24')
iget.place(x=30, y=110)

descr = tk.Label(main, text='Добро пожаловать!', font=(18), fg='black', bg='#E0E0E0')
descr.place(x=30, y=10)

igen = tk.Label(main, text='Сгенерировать(~0.3sec) >>>', font=(18), fg='black', bg='#E0E0E0')
igen.place(x=30, y=210)

addb = tk.Button(main, text='Next', command = AddIdea,  font=(18), fg='black', bg='#E0E0E0', width='24', height=1)
addb.place(x=30, y=140)

show = tk.Button(main, text='Start', command = Randi,  font=(18), fg='black', bg='#E0E0E0', width='24', height=1)
show.place(x=30, y=250)

main.mainloop()