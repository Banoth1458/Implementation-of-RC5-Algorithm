import encr
import random
import string
import tkinter
import decr
from GUI import connect

cli = tkinter.Tk()
cli.title("CLIENTSIDE")

def recieve():
    cipher = connect.client()
    c = tkinter.Tk()
    c.title("client recieved")
    tkinter.Message(c,text = cipher, width =1000).pack()
    c.mainloop()

b5 = tkinter.Button(cli, text ="recieve", command = recieve).grid(row=5,column=2)
cli.mainloop()