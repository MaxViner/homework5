from collections import Counter, namedtuple
import heapq

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

    text = input("введите текст:-->")

    code = Dawid_Hafman_coding(text)
    print(code)
    ancod = "".join(code[ch]for ch in text)
    print(len(code),len(ancod))
    for ch in sorted(code):
        print("{}: {}".format(ch,code[ch]))
    print(ancod)
    file = open("code.txt", "w")
    for element in ancod:
        file.write(element)
    qwes = input("декодировать?")
    file = open("code.txt","r")
    haf_code=file.read()
    if "д" or "y" in qwes:
        for ch in sorted(code):
            print("{}: {}".format( code[ch],ch))
        print(decoding(haf_code,code))

if __name__== "__main__":
    main()