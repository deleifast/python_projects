#encoding: iso-8859-1
import os, shutil
import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('400x50')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Manutenção no arquivos, aguarde...', fg="red", font='Arial 18')
msg.place(x=1, y=10)

os.chdir('C:/PDV')

if os.path.exists("C:/PDV/work"):
	current_directory = os.path.dirname(os.path.abspath(__file__))
	shutil.rmtree(current_directory + '/WORK/')
else:
	pass

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.endswith('loja03_pdv.zip'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.endswith('loja03_pdv.rar'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.startswith('!UVNCPFT'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.startswith('Clisitef32.dll'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.startswith('CliSiTef32.dll'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV'):
    for arquivo in arquivos:
        if arquivo.startswith('clisitef32.dll'):
           os.remove(os.path.join(raiz, arquivo))

os.startfile(r"deleta_SALCOMM_LOG.exe")		   

os.chdir('C:/PDV/PLUGIN')

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('loja03_plugin.zip'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('loja03_plugin.rar'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('aatac.dll'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('Estac.dll'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('PrepNF.dll'):
           os.remove(os.path.join(raiz, arquivo))
		   
for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.endswith('TeleVendas.DLL'):
           os.remove(os.path.join(raiz, arquivo))

for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
    for arquivo in arquivos:
        if arquivo.startswith('!UVNCPFT'):
           os.remove(os.path.join(raiz, arquivo))

def sair():
	gui.destroy()
	return

gui.after(3000, sair)


gui.mainloop()
