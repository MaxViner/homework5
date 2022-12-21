from collections import Counter, namedtuple
import heapq
from tkinter import *



class Node(namedtuple("Node", ["left","right"])):
    def walk(self,code,acc):
        self.left.walk(code, acc +"0")
        self.right.walk(code,acc+"1")


class Leaf ( namedtuple("Leaf",["char"])):
    def walk(self,code,acc):
        code[self.char]= acc or "0"
def Dawid_Hafman_coding(text):
    h=[]
    for ch ,freq in Counter(text).items():
        h.append((freq,len(h),Leaf(ch)))
    # h=[(freq,Leaf(ch)) for ch, freq in Counter(text).items()]
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2_, rigth =heapq.heappop(h)
        heapq.heappush(h, (freq1+freq2,count,Node( left, rigth)))
        count+=1


    code ={}
    if h:
        [(_freq,count,root)]=h
        root.walk(code,"")
    return code


def decoding(text,code):
    dc_decoding = {  code[key]:key for key in code}
    st_res = ''
    while len(text) > 0:
        num=1
        while text[:num] not in dc_decoding:
            num+=1
        st_res += dc_decoding[text[:num]]
        text = text[num:]
    return st_res

def main():

    text=t.get("1.0",END)
    # CODING----------------------------------
    code = Dawid_Hafman_coding(text)
    print(code)
    ancod = "".join(code[ch]for ch in text)
    print(len(code),len(ancod))
    for ch in sorted(code):
        print("{}: {}".format(ch,code[ch]))
    print(ancod)
    t1.delete("1.0", END)
    t1.insert("1.0", ancod)
    file = open("code.txt", "w")
    for element in ancod:
        file.write(element)
   # DECODING-------------------------------------



def decode_mod():
    text = t.get("1.0", END)

    code = Dawid_Hafman_coding(text)

    file = open("code.txt", "r")
    haf_code = file.read()
    for ch in sorted(code):
        print("{}: {}".format(code[ch], ch))
    print(decoding(haf_code, code))
    dec.delete("1.0", END)
    dec.insert("1.0", decoding(haf_code, code))

root = Tk()
root.geometry('700x700')
root.title('task1')
root.resizable(width=False, height=False)
root['bg']='black'


label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='поле ввода текста')
label.place(relx=0.5, y=30, anchor=CENTER )

t = Text(root,width=36 ,height=5, font="Arial 12 bold")
t.place(relx=0.5 , y=100, anchor=CENTER)
btn = Button(root, width=45, text="кодировать по Девиду Хафману" ,command=main)
btn.place(relx=0.5, y=280, anchor=CENTER)

t1 = Text(root,width=36 ,height=5, font="Arial 12 bold")
t1.place(relx=0.5 , y=360, anchor=CENTER)

dec = Text(root,width=36 ,height=5, font="Arial 12 bold")
dec.place(relx=0.5 , y=550, anchor=CENTER)
btn2 = Button(root, width=45, text="декодировать" ,command=decode_mod)
btn2.place(relx=0.5, y=480, anchor=CENTER)

root.mainloop()