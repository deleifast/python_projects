#encoding: iso-8859-1
import os
import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('400x50')
gui.title('Remarca-Alterdata')
gui.resizable(0,0)

msg = Label(gui, text='Removendo BACKUPS, aguarde...', fg="red", font='Arial 18')
msg.place(x=1, y=10)

for raiz, diretorios, arquivos in os.walk('C:\ALTERDAT\BACKUP'):
    for arquivo in arquivos:
        if arquivo.startswith('REMARCA12'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:\ALTERDAT\BACKUP'):
    for arquivo in arquivos:
        if arquivo.startswith('REMARCA18'):
           os.remove(os.path.join(raiz, arquivo))

def sair():
	gui.destroy()
	return

gui.after(3000, sair)


gui.mainloop()
