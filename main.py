from tkinter import *
import subprocess



def openXnuls():
    subprocess.Popen('dist/xnuls/xnuls.exe')

def off():
    subprocess.Popen('dist/off_AbB/off_AbB.exe')

def SweetGame():
    subprocess.Popen('dist/task2/task2.exe')
def DawidCode():
    subprocess.Popen('dist/HafmanCoding/HafmanCoding.exe')
root= Tk()
root.config(bg="grey")
root.title("ДЗ 5")
root.geometry("650x500")
root.resizable(width=False, height=False)


btn = Button(root, width=45, text="открыть крестики нолики" ,command=openXnuls, )
btn.place(relx=0.5, y=80, anchor=CENTER)

btn1 = Button(root, width=70, text="программа удаляющая из текста все слова, содержащие ""абв""." ,command=off)
btn1.place(relx=0.5, y=180, anchor=CENTER)

btn2 = Button(root, width=45, text="игра в конфетки" ,command=SweetGame)
btn2.place(relx=0.5, y=280, anchor=CENTER)

btn3 = Button(root, width=45, text="Кодирование Хафмана" ,command=DawidCode)
btn3.place(relx=0.5, y=380, anchor=CENTER)



root.mainloop()

