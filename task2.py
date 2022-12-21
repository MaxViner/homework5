import random
import time
from tkinter import *

qwote = 2021
bot_active=False
def getStep1():
    global qwote
    global bot_active

    if bot_active==False:
        print('persons')
        mid.delete("1.0", END)
        mid.insert("1.0", qwote)
        value = int(player1.get("1.0",END))
        mid.delete("1.0", END)
        if value<=28:
            qwote-=value
            if qwote<=0:
                print("победаигрока 1!")
            mid.insert("1.0", qwote)
            mid.insert("1.0", '\n ход игрока 2 \n')
            return qwote

    else:
        print('bot')
        mid.delete("1.0", END)
        mid.insert("1.0", qwote)
        value = int(player1.get("1.0", END))
        mid.delete("1.0", END)
        if value <= 28:
            qwote -= value
            if qwote <= 0:
                rez = "wow you win!!!"
                return
                mid.insert("1.0", rez)
        mid.insert("1.0", qwote)
        mid.insert("1.0", f'\n ваш ход...-{value}! \n')

        if qwote > 29 and qwote <= 57:
            value = qwote - 29
        elif qwote < 29:
            value = qwote
        elif value == 28:
            value = 28
        else:
            value = 28 - value

        qwote -= value
        if qwote <= 0:
            rez="bot vin:p"
            mid.insert("1.0", rez)
            btn["state"] = DISABLED
        mid.insert("1.0", qwote)
        time.sleep(0.3)
        mid.insert("1.0", f'\n ход бота...!-{value} \n')
        return qwote


def getStep2():
    global qwote
    mid.delete("1.0", END)
    mid.insert("1.0", qwote)
    value = int(player2.get("1.0",END))
    mid.delete("1.0", END)
    if value <= 28:
        qwote -= value
        if qwote <= 0:
            print("победаигрока 2!")
        qwote-=value
        mid.insert("1.0", qwote)
        mid.insert("1.0", '\n ход игрока 1 \n')
        return qwote


def bot_mode():
    global bot_active
    bot_active=True
    btn2["state"] = DISABLED




root = Tk()
root.geometry('800x700')
root.title('task1')
root.resizable(width=False, height=False)
root['bg']='black'



ferst=random.randint(1,2)
label = Label(root, fg='white', bg='black', font='Arial 15 bold', text=f'первым ходит игрок{ferst}')
label.place(relx=0.5, y= 30, anchor=CENTER )

player1 = Text(root,width=36 ,height=5, font="Arial 12 bold")
player1.place(relx=0.5 , y=100, anchor=CENTER)


player2 = Text(root,width=36 ,height=5, font="Arial 12 bold")
player2.place(relx=0.5 , y=500, anchor=CENTER)


btn = Button(root, width=45, text="сделать ход" ,command=getStep1)
btn.place(relx=0.5, y=180, anchor=CENTER)

btn2 = Button(root, width=45, text="сделать ход" ,command=getStep2)
btn2.place(relx=0.5, y=610, anchor=CENTER)

mid = Text(root,width=80 ,height=10, font="Arial 13 bold")
mid.place(relx=0.5 , y=350, anchor=CENTER)
instruct="Условие задачи: На столе лежит 2021 конфета." \
         " Играют два игрока делая ход \nдруг после друга. " \
         "Первый ход определяется жеребьёвкой.\n За один ход можно забрать\n не более чем 28 конфет. " \
         "\nВсе конфеты оппонента достаются сделавшему последний ход"
mid.delete("1.0", END)
mid.insert("1.0", instruct)

bot_rejim = Button(root, width=45, text="играть с ботом" ,command=bot_mode)
bot_rejim.place(relx=0.5, y=10, anchor=CENTER)


root.mainloop()
