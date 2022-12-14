import random
from tkinter import *
from random import randint as rnd

def game_stop():
    global game_left
    for i in game_left:
        buttons[i].config(bg='white', state='disabled')

def is_win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or \
        (game[3] == n and game[4] == n and game[5] == n) or \
        (game[6] == n and game[7] == n and game[8] == n) or \
        (game[0] == n and game[3] == n and game[6] == n) or \
        (game[1] == n and game[4] == n and game[7] == n) or \
        (game[2] == n and game[5] == n and game[8] == n) or \
        (game[0] == n and game[4] == n and game[8] == n) or \
        (game[2] == n and game[4] == n and game[6] == n):
        return True

def click(btn):
    global game
    global game_left
    global turn

    game[btn] = 'X'
    buttons[btn].config(text='X', bg='white', state='disabled')
    game_left.remove(btn)

    if btn == 4 and turn == 0:
        cmp = random.choice(game_left)
    elif btn != 4 and turn == 0:
        cmp = 4

    if turn > 0:
        cmp = 8 - btn
    if cmp not in game_left:
        try:
            cmp = random.choice(game_left)
        except IndexError:
            lbl.config(text='Игра окончена!')
            game_stop()

    game[cmp] = 'O'
    buttons[cmp].config(text='O', bg='white', state='disabled')

    if is_win('X'):
        lbl['text'] = 'Игрок победил!'
        game_stop()
    elif is_win('O'):
        lbl['text'] = 'Победил компьютер!'
        game_stop()
    else:
        if len(game_left) > 1:
            game_left.remove(cmp)
        else:
            lbl.config(text='Игра окончена!')
            game_stop()
        turn += 1

game = [None] * 9
game_left = list(range(9))
turn = 0

window = Tk()
window.title('Крестики - нолики')

lbl = Label(text='Крестики-нолики', width=20, font=('Arial', 20, 'bold'))
lbl.grid(row=0, column=0, columnspan=3)

buttons = [Button(font=('Roboto', 30, 'bold'), width=5, height=2, bg='#ffd200',
                  command=lambda x=i: click(x)) for i in range(9)]

row = 1
col = 0

for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

window.mainloop()
