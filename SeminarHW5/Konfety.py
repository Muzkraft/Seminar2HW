# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import *
from tkinter import *

left = 150

def who_goes_first():
    turn = randint(0, 1)
    return turn

def player():
    global left
    take = value.get()
    if int(take) > 28 or int(take) > left:
        txt_lbl.config(text='Рожа не треснет?')
    else:
        left = left - int(take)
        vsego.config(text=str(left))
        txt_lbl.config(text='Сколько конфет будем брать?')
        konfety.config(text=left * '>o< ')

    if left == 0:
        konfety.config(text='Игрок победил', fg='red', bg="green", font=100)
    else:
        move_lbl.config(text='Ходит компьютер')
        value.config(state='disabled')
        butt1.config(state='disabled')
        ai_butt.config(state='normal')

def ai():
    global left

    if left <= 28:
        ai_take = int(left)
        left = left - int(ai_take)
        vsego.config(text=str(left))
        konfety.config(text=left * '>o<')
    elif 29 < left < 57:
        ai_take = left - 29
        left = left - int(ai_take)
        vsego.config(text=str(left))
        konfety.config(text=left * '>o<')
    else:
        ai_take = randint(1, 28)
        left = left - int(ai_take)
        vsego.config(text=str(left))
        konfety.config(text=left * '>o<')

    if left == 0:
        konfety.config(text='Компьютер победил', fg='red', bg="green", font=100)
    else:
        move_lbl.config(text='Ходит человек')
        value.config(state='normal')
        butt1.config(state='normal')
        ai_butt.config(state='disabled')

pole = Tk()
pole.config(bg="green")
pole.geometry('500x300')

vsego = Label(pole, text=f'{str(left)} конфет на столе', bg="green")
vsego.pack()

move_lbl = Label(pole, text='Поехали!', bg="green")
move_lbl.pack()

txt_lbl = Label(pole, text='Сколько конфет будем брать?', bg="green")
txt_lbl.pack()

value = Entry(pole, width=5)
value.pack()

butt1 = Button(pole, text='Взять', command=player, bg='light green')
butt1.pack()

ai_butt = Button(pole, text='Ход компьютера', command=ai, bg='sienna2')
ai_butt.pack()

frame = Frame(pole,  borderwidth=4, relief=RAISED)
frame.pack()
konfety = Label(master=frame, text=left * '>o< ', fg="tomato", width=100, height=100)
konfety.config(font=('Roboto', 10))
konfety.pack()

pole.resizable(0, 0)
pole.title('Конфеты')
pole.mainloop()