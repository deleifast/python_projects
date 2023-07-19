#coding: utf8
import tkinter        #1
from tkinter import messagebox

top = tkinter.Tk()    #3
def hello(): #4       
   messagebox.showinfo("voce clicou", "Hello World")#5

B1 = tkinter.Button(top, text = "Clique Aqui!!!", command = hello)
B1.pack()

top.mainloop()