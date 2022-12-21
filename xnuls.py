import tkinter
from tkinter import *
import random,time
checker = False
mark= [None for i in range(9)]
chek1 =0
chek2 =0
buttons = []

def clic(x):
    text.delete("1.0", END)
    text.insert("1.0", "gamestart")

    win=''
    global buttons
    global chek1
    global chek2
    global mark
    global steps
    global checker
    global free_steps
    if x==0:
        if checker == False:
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker =True
            mark[0]=1
            print(mark)
            if ((mark[1]==1 and mark[2]==1)
            or (mark[3]==1 and mark[6]==1)
            or (mark[4]==1 and mark[8]==1)):
                win ="победа первого игрока!!!"
                print('1')
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1+=1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)

        else:
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker =False
            mark[0]=0
            print(mark)
            if ((mark[1]==0 and mark[2]==0)
            or (mark[3]==0 and mark[6]==0)
            or (mark[4]==0 and mark[8]==0)):
                text.delete("1.0", END)
                text.insert("1.0", "победа второго игрока!!!")
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 1:
        if checker == False:
            mark[1]=1
            print(mark)
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[0]==1 and mark[2]==1)
            or (mark[4]==1 and mark[7]==1)):
                win ="победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)

        else:
            mark[1]=0
            print(mark)
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[0]==0 and mark[2]==0)
            or (mark[4]==0 and mark[7]==0)):
                text.delete("1.0", END)
                text.insert("1.0", "победа второго игрока!!!")
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 2:
        mark[2]=1
        print(mark)
        if checker == False:
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[1] == 1 and mark[0] == 1)
                    or (mark[5] == 1 and mark[8] == 1)
                    or (mark[4] == 1 and mark[6] == 1)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)

        else:
            mark[2]=0
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[1] == 0 and mark[0] == 0)
                    or (mark[5] == 0 and mark[8] == 0)
                    or (mark[4] == 0 and mark[6] == 0)):
                win = "победа второго игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 3:
        if checker == False:
            mark[3]=1
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[5] == 1 and mark[4] == 1)
                    or (mark[0] == 1 and mark[6] == 1)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            mark[3]=0
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[5] == 0 and mark[4] == 0)
                    or (mark[0] == 0 and mark[6] == 0)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 4:
        mark[4]=1
        if checker == False:
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[1] == 1 and mark[7] == 1)
                    or (mark[0] == 1 and mark[8] == 1)
                    or (mark[3] == 1 and mark[5] == 1)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            mark[4]=0
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[1] == 0 and mark[7] == 0)
                    or (mark[0] == 0 and mark[8] == 0)
                    or (mark[3] == 0 and mark[5] == 0)):
                win = "победа 2 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 5:
        if checker == False:
            mark[5]=1
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[3] ==1 and mark[4] == 1)
                    or (mark[2] == 1 and mark[8] == 1)):
                win = "победа 1 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            mark[5]=0
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[3] == 0 and mark[4] == 0)
                    or (mark[2] == 0 and mark[8] == 0)):
                win = "победа 2 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 6:
        if checker == False:
            mark[6]=1
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[0] == 1 and mark[3] == 1)
                    or (mark[4] == 1 and mark[2] == 1)
                    or (mark[7] == 1 and mark[8] == 1)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            mark[6]=0
            steps[x] = '0'
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[0] == 0 and mark[3] == 0)
                    or (mark[4] == 0 and mark[2] == 0)
                    or (mark[7] == 0 and mark[8] == 0)):
                win = "победа 2 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 7:
        if checker == False:
            mark[7]=1
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[6] ==1 and mark[8] == 1)
                    or (mark[4] == 1 and mark[1] == 1)):
                win = "победа 1 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            steps[x] = '0'
            mark[7]=0
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[6] ==0 and mark[8] == 0)
                    or (mark[4] == 0 and mark[1] == 0)):
                win = "победа 2 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)

    if x == 8:
        if checker == False:
            mark[8]=1
            steps[x] = 'X'
            buttons[x].config(text="X", state="disabled")
            checker = True
            if ((mark[0] == 1 and mark[4] == 1)
                    or (mark[2] == 1 and mark[5] == 1)
                    or (mark[7] == 1 and mark[6] == 1)):
                win = "победа первого игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek1 += 1
                count1.delete("1.0", END)
                count1.insert("1.0", chek1)
        else:
            steps[x] = '0'
            mark[8]=0
            buttons[x].config(text="0", state="disabled")
            checker = False
            if ((mark[0] == 0 and mark[4] == 0)
                    or (mark[2] == 0 and mark[5] == 0)
                    or (mark[7] == 0 and mark[6] == 0)):
                win = "победа 2 игрока!!!"
                text.delete("1.0", END)
                text.insert("1.0", win)
                chek2 += 1
                count2.delete("1.0", END)
                count2.insert("1.0", chek2)
   

def reset():

    global buttons
    global mark
    for i in range(9):
        buttons[i].config(text="", state="normal")
        mark[i]=None


steps = [None]*9
free_steps = list(range(9))

root = Tk()
root.geometry('500x700')
label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='krestiki-noliki')
buttons = [Button(width=10,height=5, font="Arial 18 bold", command=lambda x=i: clic(x)) for i in range(9)]

text = Text(root,width=12 ,height=2, font="Arial 12 bold")
text.place(relx=0.5 , y=560, anchor=N)

count1 = Text(root,width=10 ,height=2, font="Arial 12 bold")
count1.place(relx=0.1 , y=580, anchor=N)

count2 = Text(root,width=10 ,height=2, font="Arial 12 bold")
count2.place(relx=0.9 , y=580, anchor=N)

btn = Button(root, width=45, text="начать игру" ,command=reset)
btn.place(relx=0.5, y=680, anchor=CENTER)

label.grid(row=0,column=0,columnspan=3)
row = 1;  col =0
for i in range(9):
    buttons[i].grid(row=row,column=col)
    col+=1
    if col == 3:
        row+=1
        col=0

root.mainloop()