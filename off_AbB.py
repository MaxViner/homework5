from tkinter import *


def tran():
    text=t.get("1.0",END)
    texlist =str(text)
    print(texlist)
    texlist=texlist.split(" ")
    print(texlist)
    tran_list = []
    for i in range(len(texlist)):
        print(texlist[i])
        if not "а" in str(texlist[i]) and not 'б' in str(texlist[i])\
                and not 'в' in str(texlist[i]):
            tran_list.append(texlist[i])
    text=' '.join(tran_list)


    t1.delete("1.0", END)
    t1.insert("1.0", text)

root = Tk()
root.geometry('500x350')
root.title('task1')
root.resizable(width=False, height=False)
root['bg']='black'


label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='---')
label.place(relx=0.5, y= 30, anchor=CENTER )

t = Text(root,width=36 ,height=5, font="Arial 12 bold")
t.place(relx=0.5 , y=100, anchor=CENTER)

btn = Button(root, width=45, text="удалить слова содержащие абв" ,command=tran)
btn.place(relx=0.5, y=180, anchor=CENTER)


t1 = Text(root,width=36 ,height=5, font="Arial 12 bold")
t1.place(relx=0.5 , y=260, anchor=CENTER)


root.mainloop()
