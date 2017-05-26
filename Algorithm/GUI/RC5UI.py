import encr
import random
import string
import tkinter
import decr
from GUI import connect

root = tkinter.Tk()
root.title("RC5")
tkinter.Label(root, text="USERINPUT:").grid(row = 1, column = 1)
tkinter.Label(root, text="RANDOM_KEY:").grid( row = 2, column = 1)
tkinter.Label(root,text="ROUNDS").grid(row=3,column=1)
roun = tkinter.Entry(root,bd=2)
roun.grid(row=3,column=2)
E1 = tkinter.Entry(root,bd=2)
E1.grid( row = 1, column = 2)
r = tkinter.StringVar()
rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
r.set(rand)
E2 = tkinter.Entry(root, bd=2, textvariable=r).grid(row=2, column=2)

def call():
    text = E1.get()
    count = roun.get()
    #print rand
    [cipher,left,right] = encr.clas(text,rand,count)
    ec_window = tkinter.Tk()
    tkinter.Message(ec_window, text=cipher, width=1000).pack()
    ec_window.mainloop(2)

def decrypt():
    text = E1.get()
    size1 = len(text)
    count = roun.get()
    [cipher, left, right] = encr.clas(text, rand, count)
    print cipher,left,right
    original = decr.decr(left,right,rand,count,size1)
    ec_window1 = tkinter.Tk()
    tkinter.Message(ec_window1, text=original, width=1000).pack()
    ec_window1.mainloop(2)
def send():
    text = E1.get()
    count = roun.get()
    size1 = len(text)
    [cipher,left,right] = encr.clas(text, rand, count)
    #print('ci',cipher)
    original = decr.decr(left, right, rand, count, size1)
    connect.server(original)


Enc = tkinter.Button(root, text="ENCRYPT",command=call)
Enc.grid(row = 4,column = 3)
b3 = tkinter.Button(root,text="DECRYPT",command=decrypt).grid(row=4,column=2)
b4 = tkinter.Button(root, text ="send", command = send).grid(row=5,column=1)
#key = Button(root, text="GENERATE", command =lambda: call1())
#key.grid(row = 2,column = 3)
root.mainloop()
