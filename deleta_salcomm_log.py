#encoding: iso-8859-1
import os, subprocess, sys, time
import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('400x50')
gui.resizable(0,0)

os.chdir('C:/PDV')

exists = os.path.isfile("deleta_salcomm_log.bat")
if exists:
	ret = subprocess.call("deleta_salcomm_log.bat")
	msg = Label(gui, text='Manutenção SALCOMM....', fg="blue", font= 'Arial 18')
	msg.pack()	
else:
	msg = Label(gui, text='Deleta_Sacomm_log ausente..', fg="blue", font= 'Arial 18')
	msg.pack()


def sair():
	gui.destroy()
	return

gui.after(3000, sair)


gui.mainloop()
