#encoding: iso-8859-1
import os, time, subprocess, shutil, os.path, sys, glob, glob2, configparser
from tkinter import messagebox
from tkinter import *
from tkinter.font import Font
import tkinter as tk
from PIL import Image, ImageTk

from tkinter.scrolledtext import ScrolledText

from fpdf import FPDF

OptionList = [
"Clique aqui",
"Loja 01",
"Loja 02",
"Loja 03",
"Loja 04",
"Loja 06",
"Loja 07",
"Loja 08",
"Loja 09",
"Loja 10",
"Loja 11",
"Loja 12",
"Loja 13",
"Loja 14",
"Loja 15",
"Loja 16",
"Loja 17",
"Loja 18",
"Loja 19",
"Loja 20",
"Loja 21",
"Loja 22",
"Loja 23",
"Loja 24",
"Loja 25",
"Loja 26",
"Loja 27",
"Loja 28",
"Loja 29",
"Loja 30",
"Loja 31",
"Loja 32",
"Loja 33",
"Loja 34",
"Loja 35",
"Loja 36",
"Loja 37",
"Loja 38",
"Loja 39",
"Loja 40",
"Loja 41",
"Loja 42",
"Loja 43",
"Loja 44",
"Loja 45",
"Loja 46",
"Loja 47",
"Loja 48",
"Loja 49",
"Loja 50",
"Loja 51",
"Loja 52",
"Loja 53",
"Loja 301"
] 


gui = Tk()

variable = tk.StringVar(gui)
variable.set(OptionList[0])

opt = tk.OptionMenu(gui, variable, *OptionList)
opt.config(width=30, font=('Helvetica', 10))
opt.place(x=900, y=215)


lblLoja = tk.Label(text="", font=('Calibri', 30), fg='red')
lblLoja.place(x=320, y=90)

def callback(*args):
    lblLoja.configure(text="A loja escolhida foi: {}".format(variable.get()))
    vl = variable.get()
    
    if vl == "Clique aqui":
        resp = messagebox.showerror("Erro", "Escolha uma loja")    
        if resp == "ok":
            res_texto(res)
    if vl == "Loja 01":
        Loja01()
    if vl == "Loja 02":
        Loja02()
    if vl == "Loja 03":
        Loja03()
    if vl == "Loja 04":
        Loja04()
    if vl == "Loja 06":
        Loja06()
    if vl == "Loja 07":
        Loja07()
    if vl == "Loja 08":
        Loja08()
    if vl == "Loja 09":
        Loja09()
    if vl == "Loja 10":
        Loja10()
    if vl == "Loja 11":
        Loja11()
    if vl == "Loja 12":
        Loja12()
    if vl == "Loja 13":
        Loja13()
    if vl == "Loja 14":
        Loja14()
    if vl == "Loja 15":
        Loja15()
    if vl == "Loja 16":
        Loja16()
    if vl == "Loja 17":
        Loja17()
    if vl == "Loja 18":
        Loja18()
    if vl == "Loja 19":
        Loja19()
    if vl == "Loja 20":
        Loja20()
    if vl == "Loja 21":
        Loja21()
    if vl == "Loja 22":
        Loja22()
    if vl == "Loja 23":
        Loja23()
    if vl == "Loja 24":
        Loja24()
    if vl == "Loja 25":
        Loja25()
    if vl == "Loja 26":
        Loja26()
    if vl == "Loja 27":
        Loja27()
    if vl == "Loja 28":
        Loja28()
    if vl == "Loja 29":
        Loja29()
    if vl == "Loja 30":
        Loja30()
    if vl == "Loja 31":
        Loja31()
    if vl == "Loja 32":
        Loja32()
    if vl == "Loja 33":
        Loja33()
    if vl == "Loja 34":
        Loja34()
    if vl == "Loja 35":
        Loja35()
    if vl == "Loja 36":
        Loja36()
    if vl == "Loja 37":
        Loja37()
    if vl == "Loja 38":
        Loja38()
    if vl == "Loja 39":
        Loja39()
    if vl == "Loja 40":
        Loja40()
    if vl == "Loja 41":
        Loja41()
    if vl == "Loja 42":
        Loja42()
    if vl == "Loja 43":
        Loja43()
    if vl == "Loja 44":
        Loja44()
    if vl == "Loja 45":
        Loja45()
    if vl == "Loja 46":
        Loja46()
    if vl == "Loja 47":
        Loja47()
    if vl == "Loja 48":
        Loja48()
    if vl == "Loja 49":
        Loja49()
    if vl == "Loja 50":
        Loja50()
    if vl == "Loja 51":
        Loja51()
    if vl == "Loja 52":
        Loja52()
    if vl == "Loja 53":
        Loja53()
    if vl == "Loja 301":
        Loja301()

              
variable.trace("w", callback)



bottomSair = Frame(gui)
bottomSair.place(x= 1250, y=220)

gui.title("Lista Versões")
gui.attributes('-fullscreen',True)
#gui.geometry("1366x768")
gui.resizable(0,0)

load = Image.open("logo-remarca.png")
render = ImageTk.PhotoImage(load)
img= Label(gui, image=render)
img.image = render
img.place(x=10, y=10)

var = IntVar()

mensagem= StringVar()
lbl = Label(gui, text="Escolha a loja: " , fg="blue", font="Calibri 20 bold")
lbl.place(x=730, y=210)

mensagem= StringVar()
lbl = Label(gui, text="Versão 2.0" , fg="black", font="Arial 8")
lbl.place(x=1, y=750)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Calibri 30", fg= "red")
lblaguarde.place(x=300, y=90)


def Aguarde(event):
    res = " Aguarde gerando arquivo......"
    res_texto(res)

lblfim = Label(gui, text= res, font="Calibri 20", fg= "red")
lblfim.place(x=300, y=90)

def Fim(event):
    res = " Finalizando o programa......   "
    res_texto(res)
    
    
def res_texto(res):
    lblaguarde.config(text=res)


mensagem= StringVar()
lbl = Label(gui, text="*****ÚLTIMAS VERSÕES*****" , fg="blue", font="Arial 15 bold")
lbl.place(x=1090, y=8)

#with open("atual.txt", "r") as atual:
#	t01 = atual.read()
texto = ScrolledText(gui, width=40, height=12, font=Font(family="Arial", size=9), fg="black", bg="white")
texto.place(x=1100, y=35)
#	texto.insert(END, t01)
texto.insert(tk.INSERT,
"""\
PDVSAL.EXE	-	29/05/2021
----------------------------------------------------------
SATSAL.DLL	-	28/05/2021
----------------------------------------------------------
SALCOMM.EXE	-	29/11/2018
----------------------------------------------------------
CLISITEF32I.DLL	-	13/11/2020
----------------------------------------------------------
APROMOS.DLL	-	18/01/2021
----------------------------------------------------------
CLITEF.DLL	-	28/04/2021
----------------------------------------------------------
LOGSAT.EXE	-	24/03/2021
----------------------------------------------------------
QRCODER.DLL	-	04/05/2021
----------------------------------------------------------
SHOWQR.EXE	-	04/05/2021
----------------------------------------------------------""")
  
texto.configure(state ='disabled')

def Loja01():

	try:
		with open("relver_loja01.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

							
	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('020 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('021 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('022 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('023 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja01.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj01.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja01.txt", "a") as stream:
						print('024 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

						

	with open("relver_loja01.txt") as lj01:
		f01 = lj01.readlines(240)
		f02 = lj01.readlines(240)
		f03 = lj01.readlines(240)
		f04 = lj01.readlines(240)
		f05 = lj01.readlines(240)
		f06 = lj01.readlines(240)
		f07 = lj01.readlines(240)
		f08 = lj01.readlines(240)
		f09 = lj01.readlines(240)
		f10 = lj01.readlines(240)
		f11 = lj01.readlines(240)
		f12 = lj01.readlines(240)
		f13 = lj01.readlines(240)
		f14 = lj01.readlines(240)
		f15 = lj01.readlines(240)
		f16 = lj01.readlines(240)
		f17 = lj01.readlines(240)
		f18 = lj01.readlines(240)
		f19 = lj01.readlines(240)
		f20 = lj01.readlines(240)
		f21 = lj01.readlines(240)
		f22 = lj01.readlines(240)
		f23 = lj01.readlines(240)
		f24 = lj01.readlines(240)


		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 01 - 24 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=10, y=250)
		
		listbox.selection_set(first=4)

def Loja02():

	try:
		with open("relver_loja02.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja02.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj02.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja02.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja02.txt") as lj02:
		f01 = lj02.readlines(240)
		f02 = lj02.readlines(240)
		f03 = lj02.readlines(240)
		f04 = lj02.readlines(240)
		f05 = lj02.readlines(240)
		f06 = lj02.readlines(240)
		f07 = lj02.readlines(240)
		f08 = lj02.readlines(240)
		f09 = lj02.readlines(240)
		f10 = lj02.readlines(240)
		f11 = lj02.readlines(240)
		f12 = lj02.readlines(240)
		f13 = lj02.readlines(240)
		f14 = lj02.readlines(240)
		f15 = lj02.readlines(240)
		f16 = lj02.readlines(240)
		f17 = lj02.readlines(240)
		f18 = lj02.readlines(240)
		f19 = lj02.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 02 - 19 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja03():

	try:
		with open("relver_loja03.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja03.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj03.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja03.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja03.txt") as lj03:
		f01 = lj03.readlines(240)
		f02 = lj03.readlines(240)
		f03 = lj03.readlines(240)
		f04 = lj03.readlines(240)
		f05 = lj03.readlines(240)
		f06 = lj03.readlines(240)
		f07 = lj03.readlines(240)
		f08 = lj03.readlines(240)
		f09 = lj03.readlines(240)
		f10 = lj03.readlines(240)
		f11 = lj03.readlines(240)
		f12 = lj03.readlines(240)
		f13 = lj03.readlines(240)
		f14 = lj03.readlines(240)
		f15 = lj03.readlines(240)
		f16 = lj03.readlines(240)
		f17 = lj03.readlines(240)
		f18 = lj03.readlines(240)
		f19 = lj03.readlines(240)
		f20 = lj03.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 03 - 20 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja04():

	try:
		with open("relver_loja04.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja04.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj04.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja04.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja04.txt") as lj04:
		f01 = lj04.readlines(240)
		f02 = lj04.readlines(240)
		f03 = lj04.readlines(240)
		f04 = lj04.readlines(240)
		f05 = lj04.readlines(240)
		f06 = lj04.readlines(240)
		f07 = lj04.readlines(240)
		f08 = lj04.readlines(240)
		f09 = lj04.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 04 - 09 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja06():

	try:
		with open("relver_loja06.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja06.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj06.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja06.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja06.txt") as lj06:
		f01 = lj06.readlines(240)
		f02 = lj06.readlines(240)
		f03 = lj06.readlines(240)
		f04 = lj06.readlines(240)
		f05 = lj06.readlines(240)
		f06 = lj06.readlines(240)
		f07 = lj06.readlines(240)
		f08 = lj06.readlines(240)
		f09 = lj06.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 06 - 09 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja07():

	try:
		with open("relver_loja07.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja07.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj07.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja07.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja07.txt") as lj07:
		f01 = lj07.readlines(240)
		f02 = lj07.readlines(240)
		f03 = lj07.readlines(240)
		f04 = lj07.readlines(240)
		f05 = lj07.readlines(240)
		f06 = lj07.readlines(240)
		f07 = lj07.readlines(240)
		f08 = lj07.readlines(240)
		f09 = lj07.readlines(240)
		f10 = lj07.readlines(240)
		f11 = lj07.readlines(240)
		f12 = lj07.readlines(240)
		f13 = lj07.readlines(240)
		f14 = lj07.readlines(240)
		f15 = lj07.readlines(240)
		f16 = lj07.readlines(240)
		f17 = lj07.readlines(240)
		f18 = lj07.readlines(240)
		f19 = lj07.readlines(240)
		f20 = lj07.readlines(240)
		f21 = lj07.readlines(240)
		f22 = lj07.readlines(240)
		f23 = lj07.readlines(240)
		f24 = lj07.readlines(240)
		f25 = lj07.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 07 - 25 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja08():

	try:
		with open("relver_loja08.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_142.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_143.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_141.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_148.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_146.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('126 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_144.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('127 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('128 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('129 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('130 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('131 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('132 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('133 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('134 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_135.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('135 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_136.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('136 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_137.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('137 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('138 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_139.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('139 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja08.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj08.verpdv_140.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja08.txt", "a") as stream:
						print('140 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja08.txt") as lj08:
		f01 = lj08.readlines(240)
		f02 = lj08.readlines(240)
		f03 = lj08.readlines(240)
		f04 = lj08.readlines(240)
		f05 = lj08.readlines(240)
		f06 = lj08.readlines(240)
		f07 = lj08.readlines(240)
		f08 = lj08.readlines(240)
		f09 = lj08.readlines(240)
		f10 = lj08.readlines(240)
		f11 = lj08.readlines(240)
		f12 = lj08.readlines(240)
		f13 = lj08.readlines(240)
		f14 = lj08.readlines(240)
		f15 = lj08.readlines(240)
		f16 = lj08.readlines(240)
		f17 = lj08.readlines(240)
		f18 = lj08.readlines(240)
		f19 = lj08.readlines(240)
		f20 = lj08.readlines(240)
		f21 = lj08.readlines(240)
		f22 = lj08.readlines(240)
		f23 = lj08.readlines(240)
		f24 = lj08.readlines(240)
		f25 = lj08.readlines(240)
		f26 = lj08.readlines(240)
		f27 = lj08.readlines(240)
		f28 = lj08.readlines(240)
		f29 = lj08.readlines(240)
		f30 = lj08.readlines(240)
		f31 = lj08.readlines(240)
		f32 = lj08.readlines(240)
		f33 = lj08.readlines(240)
		f34 = lj08.readlines(240)
		f35 = lj08.readlines(240)
		f36 = lj08.readlines(240)
		f37 = lj08.readlines(240)
		f38 = lj08.readlines(240)
		f39 = lj08.readlines(240)
		f40 = lj08.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 08 - 40 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)
		listbox.insert(29, f26)
		listbox.insert(30, f27)
		listbox.insert(31, f28)
		listbox.insert(32, f29)
		listbox.insert(33, f30)
		listbox.insert(34, f31)
		listbox.insert(35, f32)
		listbox.insert(36, f33)
		listbox.insert(37, f34)
		listbox.insert(38, f35)
		listbox.insert(39, f36)
		listbox.insert(40, f37)
		listbox.insert(41, f38)
		listbox.insert(42, f39)
		listbox.insert(43, f40)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja09():

	try:
		with open("relver_loja09.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja09.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj09.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja09.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja09.txt") as lj09:
		f01 = lj09.readlines(240)
		f02 = lj09.readlines(240)
		f03 = lj09.readlines(240)
		f04 = lj09.readlines(240)
		f05 = lj09.readlines(240)
		f06 = lj09.readlines(240)
		f07 = lj09.readlines(240)
		f08 = lj09.readlines(240)
		f09 = lj09.readlines(240)
		f10 = lj09.readlines(240)
		f11 = lj09.readlines(240)
		f12 = lj09.readlines(240)
		f13 = lj09.readlines(240)
		f14 = lj09.readlines(240)
		f15 = lj09.readlines(240)
		f16 = lj09.readlines(240)
		f17 = lj09.readlines(240)
		f18 = lj09.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 09 - 18 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja10():

	try:
		with open("relver_loja10.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja10.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj10.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja10.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja10.txt") as lj10:
		f01 = lj10.readlines(240)
		f02 = lj10.readlines(240)
		f03 = lj10.readlines(240)
		f04 = lj10.readlines(240)
		f05 = lj10.readlines(240)
		f06 = lj10.readlines(240)
		f07 = lj10.readlines(240)
		f08 = lj10.readlines(240)
		f09 = lj10.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 10 - 09 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja11():

	try:
		with open("relver_loja11.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_136.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_142.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_139.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_142.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_135.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('126 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_144.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('127 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('128 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('129 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('130 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja11.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj11.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja11.txt", "a") as stream:
						print('131 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)



	with open("relver_loja11.txt") as lj11:
		f01 = lj11.readlines(240)
		f02 = lj11.readlines(240)
		f03 = lj11.readlines(240)
		f04 = lj11.readlines(240)
		f05 = lj11.readlines(240)
		f06 = lj11.readlines(240)
		f07 = lj11.readlines(240)
		f08 = lj11.readlines(240)
		f09 = lj11.readlines(240)
		f10 = lj11.readlines(240)
		f11 = lj11.readlines(240)
		f12 = lj11.readlines(240)
		f13 = lj11.readlines(240)
		f14 = lj11.readlines(240)
		f15 = lj11.readlines(240)
		f16 = lj11.readlines(240)
		f17 = lj11.readlines(240)
		f18 = lj11.readlines(240)
		f19 = lj11.readlines(240)
		f20 = lj11.readlines(240)
		f21 = lj11.readlines(240)
		f22 = lj11.readlines(240)
		f23 = lj11.readlines(240)
		f24 = lj11.readlines(240)
		f25 = lj11.readlines(240)
		f26 = lj11.readlines(240)
		f27 = lj11.readlines(240)
		f28 = lj11.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 11 - 28 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)
		listbox.insert(29, f26)
		listbox.insert(30, f27)
		listbox.insert(31, f28)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja12():

	try:
		with open("relver_loja12.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja12.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj12.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja12.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja12.txt") as lj12:
		f01 = lj12.readlines(240)
		f02 = lj12.readlines(240)
		f03 = lj12.readlines(240)
		f04 = lj12.readlines(240)
		f05 = lj12.readlines(240)
		f06 = lj12.readlines(240)
		f07 = lj12.readlines(240)
		f08 = lj12.readlines(240)
		f09 = lj12.readlines(240)
		f10 = lj12.readlines(240)
		f11 = lj12.readlines(240)
		f12 = lj12.readlines(240)
		f13 = lj12.readlines(240)
		f14 = lj12.readlines(240)
		f15 = lj12.readlines(240)
		f16 = lj12.readlines(240)
		f17 = lj12.readlines(240)
		f18 = lj12.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 12 - 18 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja13():

	try:
		with open("relver_loja13.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja13.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj13.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja13.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja13.txt") as lj13:
		f01 = lj13.readlines(240)
		f02 = lj13.readlines(240)
		f03 = lj13.readlines(240)
		f04 = lj13.readlines(240)
		f05 = lj13.readlines(240)
		f06 = lj13.readlines(240)
		f07 = lj13.readlines(240)
		f08 = lj13.readlines(240)
		f09 = lj13.readlines(240)
		f10 = lj13.readlines(240)
		f11 = lj13.readlines(240)
		f12 = lj13.readlines(240)
		f13 = lj13.readlines(240)
		f14 = lj13.readlines(240)
		f15 = lj13.readlines(240)
		f16 = lj13.readlines(240)
		f17 = lj13.readlines(240)
		f18 = lj13.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 13 - 20 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja14():

	try:
		with open("relver_loja14.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja14.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj14.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja14.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja14.txt") as lj14:
		f01 = lj14.readlines(240)
		f02 = lj14.readlines(240)
		f03 = lj14.readlines(240)
		f04 = lj14.readlines(240)
		f05 = lj14.readlines(240)
		f06 = lj14.readlines(240)
		f07 = lj14.readlines(240)
		f08 = lj14.readlines(240)
		f09 = lj14.readlines(240)
		f10 = lj14.readlines(240)
		f11 = lj14.readlines(240)
		f12 = lj14.readlines(240)
		f13 = lj14.readlines(240)
		f14 = lj14.readlines(240)
		f15 = lj14.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 14 - 15 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja15():

	try:
		with open("relver_loja15.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja15.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj15.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja15.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja15.txt") as lj15:
		f01 = lj15.readlines(240)
		f02 = lj15.readlines(240)
		f03 = lj15.readlines(240)
		f04 = lj15.readlines(240)
		f05 = lj15.readlines(240)
		f06 = lj15.readlines(240)
		f07 = lj15.readlines(240)
		f08 = lj15.readlines(240)
		f09 = lj15.readlines(240)
		f10 = lj15.readlines(240)
		f11 = lj15.readlines(240)
		f12 = lj15.readlines(240)
		f13 = lj15.readlines(240)
		f14 = lj15.readlines(240)
		f15 = lj15.readlines(240)
		f16 = lj15.readlines(240)
		f17 = lj15.readlines(240)
		f18 = lj15.readlines(240)
		f19 = lj15.readlines(240)
		f20 = lj15.readlines(240)
		f21 = lj15.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 15 - 21 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja16():

	try:
		with open("relver_loja16.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja16.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj16.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja16.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja16.txt") as lj16:
		f01 = lj16.readlines(240)
		f02 = lj16.readlines(240)
		f03 = lj16.readlines(240)
		f04 = lj16.readlines(240)
		f05 = lj16.readlines(240)
		f06 = lj16.readlines(240)
		f07 = lj16.readlines(240)
		f08 = lj16.readlines(240)
		f09 = lj16.readlines(240)
		f10 = lj16.readlines(240)
		f11 = lj16.readlines(240)
		f12 = lj16.readlines(240)
		f13 = lj16.readlines(240)
		f14 = lj16.readlines(240)
		f15 = lj16.readlines(240)
		f16 = lj16.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 16 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja17():

	try:
		with open("relver_loja17.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja17.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj17.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja17.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja17.txt") as lj17:
		f01 = lj17.readlines(240)
		f02 = lj17.readlines(240)
		f03 = lj17.readlines(240)
		f04 = lj17.readlines(240)
		f05 = lj17.readlines(240)
		f06 = lj17.readlines(240)
		f07 = lj17.readlines(240)
		f08 = lj17.readlines(240)
		f09 = lj17.readlines(240)
		f10 = lj17.readlines(240)
		f11 = lj17.readlines(240)
		f12 = lj17.readlines(240)
		f13 = lj17.readlines(240)
		f14 = lj17.readlines(240)
		f15 = lj17.readlines(240)
		f16 = lj17.readlines(240)
		f17 = lj17.readlines(240)
		f18 = lj17.readlines(240)
		f19 = lj17.readlines(240)
		f20 = lj17.readlines(240)
		f21 = lj17.readlines(240)
		f22 = lj17.readlines(240)
		f23 = lj17.readlines(240)
		f24 = lj17.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 17 - 24 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja18():

	try:
		with open("relver_loja18.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja18.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj18.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja18.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja18.txt") as lj18:
		f01 = lj18.readlines(240)
		f02 = lj18.readlines(240)
		f03 = lj18.readlines(240)
		f04 = lj18.readlines(240)
		f05 = lj18.readlines(240)
		f06 = lj18.readlines(240)
		f07 = lj18.readlines(240)
		f08 = lj18.readlines(240)
		f09 = lj18.readlines(240)
		f10 = lj18.readlines(240)
		f11 = lj18.readlines(240)
		f12 = lj18.readlines(240)
		f13 = lj18.readlines(240)
		f14 = lj18.readlines(240)
		f15 = lj18.readlines(240)
		f16 = lj18.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 18 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)


def Loja19():

	try:
		with open("relver_loja19.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja19.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj19.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja19.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja19.txt") as lj19:
		f01 = lj19.readlines(240)
		f02 = lj19.readlines(240)
		f03 = lj19.readlines(240)
		f04 = lj19.readlines(240)
		f05 = lj19.readlines(240)
		f06 = lj19.readlines(240)
		f07 = lj19.readlines(240)
		f08 = lj19.readlines(240)
		f09 = lj19.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 19 - 09 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)


def Loja20():

	try:
		with open("relver_loja20.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja20.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj20.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja20.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja20.txt") as lj20:
		f01 = lj20.readlines(240)
		f02 = lj20.readlines(240)
		f03 = lj20.readlines(240)
		f04 = lj20.readlines(240)
		f05 = lj20.readlines(240)
		f06 = lj20.readlines(240)
		f07 = lj20.readlines(240)
		f08 = lj20.readlines(240)
		f09 = lj20.readlines(240)
		f10 = lj20.readlines(240)
		f11 = lj20.readlines(240)
		f12 = lj20.readlines(240)
		f13 = lj20.readlines(240)
		f14 = lj20.readlines(240)
		f15 = lj20.readlines(240)
		f16 = lj20.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 20 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)


def Loja21():

	try:
		with open("relver_loja21.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja21.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj21.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja21.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja21.txt") as lj21:
		f01 = lj21.readlines(240)
		f02 = lj21.readlines(240)
		f03 = lj21.readlines(240)
		f04 = lj21.readlines(240)
		f05 = lj21.readlines(240)
		f06 = lj21.readlines(240)
		f07 = lj21.readlines(240)
		f08 = lj21.readlines(240)
		f09 = lj21.readlines(240)
		f10 = lj21.readlines(240)
		f11 = lj21.readlines(240)
		f12 = lj21.readlines(240)
		f13 = lj21.readlines(240)
		f14 = lj21.readlines(240)
		f15 = lj21.readlines(240)
		f16 = lj21.readlines(240)
		f17 = lj21.readlines(240)
		f18 = lj21.readlines(240)
		f19 = lj21.readlines(240)
		f20 = lj21.readlines(240)
		f21 = lj21.readlines(240)
		f22 = lj21.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 21 - 22 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja22():

	try:
		with open("relver_loja22.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja22.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj22.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja22.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja22.txt") as lj22:
		f01 = lj22.readlines(240)
		f02 = lj22.readlines(240)
		f03 = lj22.readlines(240)
		f04 = lj22.readlines(240)
		f05 = lj22.readlines(240)
		f06 = lj22.readlines(240)
		f07 = lj22.readlines(240)
		f08 = lj22.readlines(240)
		f09 = lj22.readlines(240)
		f10 = lj22.readlines(240)
		f11 = lj22.readlines(240)
		f12 = lj22.readlines(240)
		f13 = lj22.readlines(240)
		f14 = lj22.readlines(240)
		f15 = lj22.readlines(240)
		f16 = lj22.readlines(240)
		f17 = lj22.readlines(240)
		f18 = lj22.readlines(240)
		f19 = lj22.readlines(240)
		f20 = lj22.readlines(240)
		f21 = lj22.readlines(240)
		f22 = lj22.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 22 - 22 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja23():

	try:
		with open("relver_loja23.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja23.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj23.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja23.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja23.txt") as lj23:
		f01 = lj23.readlines(240)
		f02 = lj23.readlines(240)
		f03 = lj23.readlines(240)
		f04 = lj23.readlines(240)
		f05 = lj23.readlines(240)
		f06 = lj23.readlines(240)
		f07 = lj23.readlines(240)
		f08 = lj23.readlines(240)
		f09 = lj23.readlines(240)
		f10 = lj23.readlines(240)
		f11 = lj23.readlines(240)
		f12 = lj23.readlines(240)
		f13 = lj23.readlines(240)
		f14 = lj23.readlines(240)
		f15 = lj23.readlines(240)
		f16 = lj23.readlines(240)
		f17 = lj23.readlines(240)
		f18 = lj23.readlines(240)
		f19 = lj23.readlines(240)
		f20 = lj23.readlines(240)
		f21 = lj23.readlines(240)
		f22 = lj23.readlines(240)
		f23 = lj23.readlines(240)
		f24 = lj23.readlines(240)
		f25 = lj23.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 23 - 25 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja24():

	try:
		with open("relver_loja24.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja24.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj24.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja24.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja24.txt") as lj24:
		f01 = lj24.readlines(240)
		f02 = lj24.readlines(240)
		f03 = lj24.readlines(240)
		f04 = lj24.readlines(240)
		f05 = lj24.readlines(240)
		f06 = lj24.readlines(240)
		f07 = lj24.readlines(240)
		f08 = lj24.readlines(240)
		f09 = lj24.readlines(240)
		f10 = lj24.readlines(240)
		f11 = lj24.readlines(240)
		f12 = lj24.readlines(240)
		f13 = lj24.readlines(240)
		f14 = lj24.readlines(240)
		f15 = lj24.readlines(240)
		f16 = lj24.readlines(240)
		f17 = lj24.readlines(240)
		f18 = lj24.readlines(240)
		f19 = lj24.readlines(240)
		f20 = lj24.readlines(240)
		f21 = lj24.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 24 - 21 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja25():

	try:
		with open("relver_loja25.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja25.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj25.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja25.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja25.txt") as lj25:
		f01 = lj25.readlines(240)
		f02 = lj25.readlines(240)
		f03 = lj25.readlines(240)
		f04 = lj25.readlines(240)
		f05 = lj25.readlines(240)
		f06 = lj25.readlines(240)
		f07 = lj25.readlines(240)
		f08 = lj25.readlines(240)
		f09 = lj25.readlines(240)
		f10 = lj25.readlines(240)
		f11 = lj25.readlines(240)
		f12 = lj25.readlines(240)
		f13 = lj25.readlines(240)
		f14 = lj25.readlines(240)
		f15 = lj25.readlines(240)
		f16 = lj25.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 25 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja26():

	try:
		with open("relver_loja26.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('126 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('127 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('128 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_135.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('129 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_139.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('130 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja26.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj26.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja26.txt", "a") as stream:
						print('131 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)



	with open("relver_loja26.txt") as lj26:
		f01 = lj26.readlines(240)
		f02 = lj26.readlines(240)
		f03 = lj26.readlines(240)
		f04 = lj26.readlines(240)
		f05 = lj26.readlines(240)
		f06 = lj26.readlines(240)
		f07 = lj26.readlines(240)
		f08 = lj26.readlines(240)
		f09 = lj26.readlines(240)
		f10 = lj26.readlines(240)
		f11 = lj26.readlines(240)
		f12 = lj26.readlines(240)
		f13 = lj26.readlines(240)
		f14 = lj26.readlines(240)
		f15 = lj26.readlines(240)
		f16 = lj26.readlines(240)
		f17 = lj26.readlines(240)
		f18 = lj26.readlines(240)
		f19 = lj26.readlines(240)
		f20 = lj26.readlines(240)
		f21 = lj26.readlines(240)
		f22 = lj26.readlines(240)
		f23 = lj26.readlines(240)
		f24 = lj26.readlines(240)
		f25 = lj26.readlines(240)
		f26 = lj26.readlines(240)
		f27 = lj26.readlines(240)
		f28 = lj26.readlines(240)
		f29 = lj26.readlines(240)
		f30 = lj26.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 26 - 30 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)
		listbox.insert(29, f26)
		listbox.insert(30, f27)
		listbox.insert(31, f28)
		listbox.insert(32, f29)
		listbox.insert(33, f30)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja27():

	try:
		with open("relver_loja27.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja27.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj27.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja27.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja27.txt") as lj27:
		f01 = lj27.readlines(240)
		f02 = lj27.readlines(240)
		f03 = lj27.readlines(240)
		f04 = lj27.readlines(240)
		f05 = lj27.readlines(240)
		f06 = lj27.readlines(240)
		f07 = lj27.readlines(240)
		f08 = lj27.readlines(240)
		f09 = lj27.readlines(240)
		f10 = lj27.readlines(240)
		f11 = lj27.readlines(240)
		f12 = lj27.readlines(240)
		f13 = lj27.readlines(240)
		f14 = lj27.readlines(240)
		f15 = lj27.readlines(240)
		f16 = lj27.readlines(240)
		f17 = lj27.readlines(240)
		f18 = lj27.readlines(240)
		f19 = lj27.readlines(240)
		f20 = lj27.readlines(240)
		f21 = lj27.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 27 - 21 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja28():

	try:
		with open("relver_loja28.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja28.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj28.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja28.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja28.txt") as lj28:
		f01 = lj28.readlines(240)
		f02 = lj28.readlines(240)
		f03 = lj28.readlines(240)
		f04 = lj28.readlines(240)
		f05 = lj28.readlines(240)
		f06 = lj28.readlines(240)
		f07 = lj28.readlines(240)
		f08 = lj28.readlines(240)
		f09 = lj28.readlines(240)
		f10 = lj28.readlines(240)
		f11 = lj28.readlines(240)
		f12 = lj28.readlines(240)
		f13 = lj28.readlines(240)
		f14 = lj28.readlines(240)
		f15 = lj28.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 28 - 15 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja29():

	try:
		with open("relver_loja29.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja29.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj29.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja29.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja29.txt") as lj29:
		f01 = lj29.readlines(240)
		f02 = lj29.readlines(240)
		f03 = lj29.readlines(240)
		f04 = lj29.readlines(240)
		f05 = lj29.readlines(240)
		f06 = lj29.readlines(240)
		f07 = lj29.readlines(240)
		f08 = lj29.readlines(240)
		f09 = lj29.readlines(240)
		f10 = lj29.readlines(240)
		f11 = lj29.readlines(240)
		f12 = lj29.readlines(240)
		f13 = lj29.readlines(240)
		f14 = lj29.readlines(240)
		f15 = lj29.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 29 - 15 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja30():

	try:
		with open("relver_loja30.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_006.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_26.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_27.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_10.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_018.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('020 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_021.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('021 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_022.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('022 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_023.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('023 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_024.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('024 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja30.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj30.verpdv_025.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja30.txt", "a") as stream:
						print('025 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja30.txt") as lj30:
		f01 = lj30.readlines(240)
		f02 = lj30.readlines(240)
		f03 = lj30.readlines(240)
		f04 = lj30.readlines(240)
		f05 = lj30.readlines(240)
		f06 = lj30.readlines(240)
		f07 = lj30.readlines(240)
		f08 = lj30.readlines(240)
		f09 = lj30.readlines(240)
		f10 = lj30.readlines(240)
		f11 = lj30.readlines(240)
		f12 = lj30.readlines(240)
		f13 = lj30.readlines(240)
		f14 = lj30.readlines(240)
		f15 = lj30.readlines(240)
		f16 = lj30.readlines(240)
		f17 = lj30.readlines(240)
		f18 = lj30.readlines(240)
		f19 = lj30.readlines(240)
		f20 = lj30.readlines(240)
		f21 = lj30.readlines(240)
		f22 = lj30.readlines(240)
		f23 = lj30.readlines(240)
		f24 = lj30.readlines(240)
		f25 = lj30.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 30 - 25 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja31():

	try:
		with open("relver_loja31.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja31.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj31.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja31.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja31.txt") as lj31:
		f01 = lj31.readlines(240)
		f02 = lj31.readlines(240)
		f03 = lj31.readlines(240)
		f04 = lj31.readlines(240)
		f05 = lj31.readlines(240)
		f06 = lj31.readlines(240)
		f07 = lj31.readlines(240)
		f08 = lj31.readlines(240)
		f09 = lj31.readlines(240)
		f10 = lj31.readlines(240)
		f11 = lj31.readlines(240)
		f12 = lj31.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 31 - 12 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja32():

	try:
		with open("relver_loja32.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja32.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj32.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja32.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja32.txt") as lj32:
		f01 = lj32.readlines(240)
		f02 = lj32.readlines(240)
		f03 = lj32.readlines(240)
		f04 = lj32.readlines(240)
		f05 = lj32.readlines(240)
		f06 = lj32.readlines(240)
		f07 = lj32.readlines(240)
		f08 = lj32.readlines(240)
		f09 = lj32.readlines(240)
		f10 = lj32.readlines(240)
		f11 = lj32.readlines(240)
		f12 = lj32.readlines(240)
		f13 = lj32.readlines(240)
		f14 = lj32.readlines(240)
		f15 = lj32.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 32 - 11 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja33():

	try:
		with open("relver_loja33.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja33.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj33.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja33.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja33.txt") as lj33:
		f01 = lj33.readlines(240)
		f02 = lj33.readlines(240)
		f03 = lj33.readlines(240)
		f04 = lj33.readlines(240)
		f05 = lj33.readlines(240)
		f06 = lj33.readlines(240)
		f07 = lj33.readlines(240)
		f08 = lj33.readlines(240)
		f09 = lj33.readlines(240)
		f10 = lj33.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 33 - 10 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja34():

	try:
		with open("relver_loja34.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja34.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj34.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja34.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja34.txt") as lj34:
		f01 = lj34.readlines(240)
		f02 = lj34.readlines(240)
		f03 = lj34.readlines(240)
		f04 = lj34.readlines(240)
		f05 = lj34.readlines(240)
		f06 = lj34.readlines(240)
		f07 = lj34.readlines(240)
		f08 = lj34.readlines(240)
		f09 = lj34.readlines(240)
		f10 = lj34.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 34 - 10 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja35():

	try:
		with open("relver_loja35.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja35.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj35.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja35.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja35.txt") as lj35:
		f01 = lj35.readlines(240)
		f02 = lj35.readlines(240)
		f03 = lj35.readlines(240)
		f04 = lj35.readlines(240)
		f05 = lj35.readlines(240)
		f06 = lj35.readlines(240)
		f07 = lj35.readlines(240)
		f08 = lj35.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 35- 08 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja36():

	try:
		with open("relver_loja36.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)
	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)
	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja36.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj36.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja36.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)


	with open("relver_loja36.txt") as lj36:
		f01 = lj36.readlines(240)
		f02 = lj36.readlines(240)
		f03 = lj36.readlines(240)
		f04 = lj36.readlines(240)
		f05 = lj36.readlines(240)
		f06 = lj36.readlines(240)
		f07 = lj36.readlines(240)
		f08 = lj36.readlines(240)
		f09 = lj36.readlines(240)
		f10 = lj36.readlines(240)
		f11 = lj36.readlines(240)
		f12 = lj36.readlines(240)
		f13 = lj36.readlines(240)
		f14 = lj36.readlines(240)
		f15 = lj36.readlines(240)
		f16 = lj36.readlines(240)
		f17 = lj36.readlines(240)
		f18 = lj36.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 36 - 18 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(NFC-e)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja37():

	try:
		with open("relver_loja37.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja37.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj37.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja37.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja37.txt") as lj37:
		f01 = lj37.readlines(240)
		f02 = lj37.readlines(240)
		f03 = lj37.readlines(240)
		f04 = lj37.readlines(240)
		f05 = lj37.readlines(240)
		f06 = lj37.readlines(240)
		f07 = lj37.readlines(240)
		f08 = lj37.readlines(240)
		f09 = lj37.readlines(240)
		f10 = lj37.readlines(240)
		f11 = lj37.readlines(240)
		f12 = lj37.readlines(240)
		f13 = lj37.readlines(240)
		f14 = lj37.readlines(240)
		f15 = lj37.readlines(240)
		f16 = lj37.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 37 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja38():

	try:
		with open("relver_loja38.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_137.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_140.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_143.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_142.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_136.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja38.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj38.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja38.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja38.txt") as lj38:
		f01 = lj38.readlines(240)
		f02 = lj38.readlines(240)
		f03 = lj38.readlines(240)
		f04 = lj38.readlines(240)
		f05 = lj38.readlines(240)
		f06 = lj38.readlines(240)
		f07 = lj38.readlines(240)
		f08 = lj38.readlines(240)
		f09 = lj38.readlines(240)
		f10 = lj38.readlines(240)
		f11 = lj38.readlines(240)
		f12 = lj38.readlines(240)
		f13 = lj38.readlines(240)
		f14 = lj38.readlines(240)
		f15 = lj38.readlines(240)
		f16 = lj38.readlines(240)
		f17 = lj38.readlines(240)
		f18 = lj38.readlines(240)
		f19 = lj38.readlines(240)
		f20 = lj38.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 38 - 20 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja39():

	try:
		with open("relver_loja39.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_130.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_137.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_135.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_140.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_129.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_136.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_139.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja39.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj39.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja39.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja39.txt") as lj39:
		f01 = lj39.readlines(240)
		f02 = lj39.readlines(240)
		f03 = lj39.readlines(240)
		f04 = lj39.readlines(240)
		f05 = lj39.readlines(240)
		f06 = lj39.readlines(240)
		f07 = lj39.readlines(240)
		f08 = lj39.readlines(240)
		f09 = lj39.readlines(240)
		f10 = lj39.readlines(240)
		f11 = lj39.readlines(240)
		f12 = lj39.readlines(240)
		f13 = lj39.readlines(240)
		f14 = lj39.readlines(240)
		f15 = lj39.readlines(240)
		f16 = lj39.readlines(240)
		f17 = lj39.readlines(240)
		f18 = lj39.readlines(240)
		f19 = lj39.readlines(240)
		f20 = lj39.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 39 - 20 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja40():

	try:
		with open("relver_loja40.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja40.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj40.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja40.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja40.txt") as lj40:
		f01 = lj40.readlines(240)
		f02 = lj40.readlines(240)
		f03 = lj40.readlines(240)
		f04 = lj40.readlines(240)
		f05 = lj40.readlines(240)
		f06 = lj40.readlines(240)
		f07 = lj40.readlines(240)
		f08 = lj40.readlines(240)
		f09 = lj40.readlines(240)
		f10 = lj40.readlines(240)
		f11 = lj40.readlines(240)
		f12 = lj40.readlines(240)
		f13 = lj40.readlines(240)
		f14 = lj40.readlines(240)
		f15 = lj40.readlines(240)
		f16 = lj40.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 40 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja41():

	try:
		with open("relver_loja41.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_008.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja41.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj41.verpdv_018.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja41.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja41.txt") as lj41:
		f01 = lj41.readlines(240)
		f02 = lj41.readlines(240)
		f03 = lj41.readlines(240)
		f04 = lj41.readlines(240)
		f05 = lj41.readlines(240)
		f06 = lj41.readlines(240)
		f07 = lj41.readlines(240)
		f08 = lj41.readlines(240)
		f09 = lj41.readlines(240)
		f10 = lj41.readlines(240)
		f11 = lj41.readlines(240)
		f12 = lj41.readlines(240)
		f13 = lj41.readlines(240)
		f14 = lj41.readlines(240)
		f15 = lj41.readlines(240)
		f16 = lj41.readlines(240)
		f17 = lj41.readlines(240)
		f18 = lj41.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 41 - 18 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja42():

	try:
		with open("relver_loja42.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_006.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_008.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja42.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj42.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja42.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja42.txt") as lj42:
		f01 = lj42.readlines(240)
		f02 = lj42.readlines(240)
		f03 = lj42.readlines(240)
		f04 = lj42.readlines(240)
		f05 = lj42.readlines(240)
		f06 = lj42.readlines(240)
		f07 = lj42.readlines(240)
		f08 = lj42.readlines(240)
		f09 = lj42.readlines(240)
		f10 = lj42.readlines(240)
		f11 = lj42.readlines(240)
		f12 = lj42.readlines(240)
		f13 = lj42.readlines(240)
		f14 = lj42.readlines(240)
		f15 = lj42.readlines(240)
		f16 = lj42.readlines(240)
		f17 = lj42.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 42 - 17 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja43():

	try:
		with open("relver_loja43.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_023.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_029.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_024.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_026.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_028.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_025.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_018.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja43.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj43.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja43.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja43.txt") as lj43:
		f01 = lj43.readlines(240)
		f02 = lj43.readlines(240)
		f03 = lj43.readlines(240)
		f04 = lj43.readlines(240)
		f05 = lj43.readlines(240)
		f06 = lj43.readlines(240)
		f07 = lj43.readlines(240)
		f08 = lj43.readlines(240)
		f09 = lj43.readlines(240)
		f10 = lj43.readlines(240)
		f11 = lj43.readlines(240)
		f12 = lj43.readlines(240)
		f13 = lj43.readlines(240)
		f14 = lj43.readlines(240)
		f15 = lj43.readlines(240)
		f16 = lj43.readlines(240)
		f17 = lj43.readlines(240)
		f18 = lj43.readlines(240)
		f19 = lj43.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 43 - 19 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja44():

	try:
		with open("relver_loja44.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_17.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_06.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_021.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja44.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj44.verpdv_18.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja44.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja44.txt") as lj44:
		f01 = lj44.readlines(240)
		f02 = lj44.readlines(240)
		f03 = lj44.readlines(240)
		f04 = lj44.readlines(240)
		f05 = lj44.readlines(240)
		f06 = lj44.readlines(240)
		f07 = lj44.readlines(240)
		f08 = lj44.readlines(240)
		f09 = lj44.readlines(240)
		f10 = lj44.readlines(240)
		f11 = lj44.readlines(240)
		f12 = lj44.readlines(240)
		f13 = lj44.readlines(240)
		f14 = lj44.readlines(240)
		f15 = lj44.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 44 - 15 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja45():

	try:
		with open("relver_loja45.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_069.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_070.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_071.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_072.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_073.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_074.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_075.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_076.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_077.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_078.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_079.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_080.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_081.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_082.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_099.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_084.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_085.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_086.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_087.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_088.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_089.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_090.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_091.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_092.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja45.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj45.verpdv_093.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja45.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)


	with open("relver_loja45.txt") as lj45:
		f01 = lj45.readlines(240)
		f02 = lj45.readlines(240)
		f03 = lj45.readlines(240)
		f04 = lj45.readlines(240)
		f05 = lj45.readlines(240)
		f06 = lj45.readlines(240)
		f07 = lj45.readlines(240)
		f08 = lj45.readlines(240)
		f09 = lj45.readlines(240)
		f10 = lj45.readlines(240)
		f11 = lj45.readlines(240)
		f12 = lj45.readlines(240)
		f13 = lj45.readlines(240)
		f14 = lj45.readlines(240)
		f15 = lj45.readlines(240)
		f16 = lj45.readlines(240)
		f17 = lj45.readlines(240)
		f18 = lj45.readlines(240)
		f19 = lj45.readlines(240)
		f20 = lj45.readlines(240)
		f21 = lj45.readlines(240)
		f22 = lj45.readlines(240)
		f23 = lj45.readlines(240)
		f24 = lj45.readlines(240)
		f25 = lj45.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 45 - 25 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)
		listbox.insert(26, f23)
		listbox.insert(27, f24)
		listbox.insert(28, f25)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja46():

	try:
		with open("relver_loja46.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_032.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_048.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_037.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_033.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_031.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_025.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_035.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_036.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_054.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_042.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_047.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_038.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_050.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_051.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_039.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_052.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_034.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('020 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_041.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('021 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja46.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj46.verpdv_029.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja46.txt", "a") as stream:
						print('022 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja46.txt") as lj46:
		f01 = lj46.readlines(240)
		f02 = lj46.readlines(240)
		f03 = lj46.readlines(240)
		f04 = lj46.readlines(240)
		f05 = lj46.readlines(240)
		f06 = lj46.readlines(240)
		f07 = lj46.readlines(240)
		f08 = lj46.readlines(240)
		f09 = lj46.readlines(240)
		f10 = lj46.readlines(240)
		f11 = lj46.readlines(240)
		f12 = lj46.readlines(240)
		f13 = lj46.readlines(240)
		f14 = lj46.readlines(240)
		f15 = lj46.readlines(240)
		f16 = lj46.readlines(240)
		f17 = lj46.readlines(240)
		f18 = lj46.readlines(240)
		f19 = lj46.readlines(240)
		f20 = lj46.readlines(240)
		f21 = lj46.readlines(240)
		f22 = lj46.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 46 - 22 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)
		listbox.insert(25, f22)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja47():

	try:
		with open("relver_loja47.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_133.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_139.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_128.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_134.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_132.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_135.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_138.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_137.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_131.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja47.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj47.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja47.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja47.txt") as lj47:
		f01 = lj47.readlines(240)
		f02 = lj47.readlines(240)
		f03 = lj47.readlines(240)
		f04 = lj47.readlines(240)
		f05 = lj47.readlines(240)
		f06 = lj47.readlines(240)
		f07 = lj47.readlines(240)
		f08 = lj47.readlines(240)
		f09 = lj47.readlines(240)
		f10 = lj47.readlines(240)
		f11 = lj47.readlines(240)
		f12 = lj47.readlines(240)
		f13 = lj47.readlines(240)
		f14 = lj47.readlines(240)
		f15 = lj47.readlines(240)
		f16 = lj47.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 47 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja48():

	try:
		with open("relver_loja48.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja48.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj48.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja48.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja48.txt") as lj48:
		f01 = lj48.readlines(240)
		f02 = lj48.readlines(240)
		f03 = lj48.readlines(240)
		f04 = lj48.readlines(240)
		f05 = lj48.readlines(240)
		f06 = lj48.readlines(240)
		f07 = lj48.readlines(240)
		f08 = lj48.readlines(240)
		f09 = lj48.readlines(240)
		f10 = lj48.readlines(240)
		f11 = lj48.readlines(240)
		f12 = lj48.readlines(240)
		f13 = lj48.readlines(240)
		f14 = lj48.readlines(240)
		f15 = lj48.readlines(240)
		f16 = lj48.readlines(240)
		f17 = lj48.readlines(240)
		f18 = lj48.readlines(240)
		f19 = lj48.readlines(240)
		f20 = lj48.readlines(240)
		f21 = lj48.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 48 - 21 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(22, f19)
		listbox.insert(23, f20)
		listbox.insert(24, f21)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja49():

	try:
		with open("relver_loja49.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_117.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('117 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_118.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('118 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_119.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('119 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_120.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('120 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_121.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('121 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_122.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('122 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_123.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('123 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_124.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('124 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_125.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('125 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_126.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('126 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja49.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj49.verpdv_127.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja49.txt", "a") as stream:
						print('127 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja49.txt") as lj49:
		f01 = lj49.readlines(240)
		f02 = lj49.readlines(240)
		f03 = lj49.readlines(240)
		f04 = lj49.readlines(240)
		f05 = lj49.readlines(240)
		f06 = lj49.readlines(240)
		f07 = lj49.readlines(240)
		f08 = lj49.readlines(240)
		f09 = lj49.readlines(240)
		f10 = lj49.readlines(240)
		f11 = lj49.readlines(240)
		f12 = lj49.readlines(240)
		f13 = lj49.readlines(240)
		f14 = lj49.readlines(240)
		f15 = lj49.readlines(240)
		f16 = lj49.readlines(240)
		f17 = lj49.readlines(240)
		f18 = lj49.readlines(240)
		f19 = lj49.readlines(240)
		f20 = lj49.readlines(240)
		f21 = lj49.readlines(240)
		f22 = lj49.readlines(240)
		f23 = lj49.readlines(240)
		f24 = lj49.readlines(240)
		f25 = lj49.readlines(240)
		f26 = lj49.readlines(240)
		f27 = lj49.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 49 - 27 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(23, f19)
		listbox.insert(24, f20)
		listbox.insert(25, f21)
		listbox.insert(26, f22)
		listbox.insert(27, f23)
		listbox.insert(28, f24)
		listbox.insert(29, f25)
		listbox.insert(30, f26)
		listbox.insert(31, f27)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja50():

	try:
		with open("relver_loja50.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_006.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_008.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_018.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('020 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_021.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('021 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_022.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('022 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_023.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('023 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_024.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('024 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_025.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('025 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_026.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('026 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja50.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj50.verpdv_027.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja50.txt", "a") as stream:
						print('027 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja50.txt") as lj50:
		f01 = lj50.readlines(240)
		f02 = lj50.readlines(240)
		f03 = lj50.readlines(240)
		f04 = lj50.readlines(240)
		f05 = lj50.readlines(240)
		f06 = lj50.readlines(240)
		f07 = lj50.readlines(240)
		f08 = lj50.readlines(240)
		f09 = lj50.readlines(240)
		f10 = lj50.readlines(240)
		f11 = lj50.readlines(240)
		f12 = lj50.readlines(240)
		f13 = lj50.readlines(240)
		f14 = lj50.readlines(240)
		f15 = lj50.readlines(240)
		f16 = lj50.readlines(240)
		f17 = lj50.readlines(240)
		f18 = lj50.readlines(240)
		f19 = lj50.readlines(240)
		f20 = lj50.readlines(240)
		f21 = lj50.readlines(240)
		f22 = lj50.readlines(240)
		f23 = lj50.readlines(240)
		f24 = lj50.readlines(240)
		f25 = lj50.readlines(240)
		f26 = lj50.readlines(240)
		f27 = lj50.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 50 - 27 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(23, f19)
		listbox.insert(24, f20)
		listbox.insert(25, f21)
		listbox.insert(26, f22)
		listbox.insert(27, f23)
		listbox.insert(28, f24)
		listbox.insert(29, f25)
		listbox.insert(30, f26)
		listbox.insert(31, f27)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja51():

	try:
		with open("relver_loja51.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_001.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_006.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_008.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_018.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('018 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_019.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('019 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_020.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('020 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_021.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('021 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_022.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('022 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_023.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('023 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_024.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('024 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_025.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('025 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_026.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('026 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)
	try:
		with open("relver_loja51.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj51.verpdv_027.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja51.txt", "a") as stream:
						print('027 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja51.txt") as lj51:
		f01 = lj51.readlines(240)
		f02 = lj51.readlines(240)
		f03 = lj51.readlines(240)
		f04 = lj51.readlines(240)
		f05 = lj51.readlines(240)
		f06 = lj51.readlines(240)
		f07 = lj51.readlines(240)
		f08 = lj51.readlines(240)
		f09 = lj51.readlines(240)
		f10 = lj51.readlines(240)
		f11 = lj51.readlines(240)
		f12 = lj51.readlines(240)
		f13 = lj51.readlines(240)
		f14 = lj51.readlines(240)
		f15 = lj51.readlines(240)
		f16 = lj51.readlines(240)
		f17 = lj51.readlines(240)
		f18 = lj51.readlines(240)
		f19 = lj51.readlines(240)
		f20 = lj51.readlines(240)
		f21 = lj51.readlines(240)
		f22 = lj51.readlines(240)
		f23 = lj51.readlines(240)
		f24 = lj51.readlines(240)
		f25 = lj51.readlines(240)
		f26 = lj51.readlines(240)
		f27 = lj51.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 51 - 27 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)
		listbox.insert(20, f17)
		listbox.insert(21, f18)
		listbox.insert(23, f19)
		listbox.insert(24, f20)
		listbox.insert(25, f21)
		listbox.insert(26, f22)
		listbox.insert(27, f23)
		listbox.insert(28, f24)
		listbox.insert(29, f25)
		listbox.insert(30, f26)
		listbox.insert(31, f27)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja52():

	try:
		with open("relver_loja52.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_002.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('002 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_003.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('003 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_004.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('004 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_005.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('005 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_006.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('006 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_007.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('007 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_008.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('008 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_009.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('009 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_010.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('010 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_011.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('011 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_012.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('012 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_013.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('013 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_014.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('014 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_015.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('015 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_016.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('016 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	try:
		with open("relver_loja52.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj52.verpdv_017.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja52.txt", "a") as stream:
						print('017 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja52.txt") as lj52:
		f01 = lj52.readlines(240)
		f02 = lj52.readlines(240)
		f03 = lj52.readlines(240)
		f04 = lj52.readlines(240)
		f05 = lj52.readlines(240)
		f06 = lj52.readlines(240)
		f07 = lj52.readlines(240)
		f08 = lj52.readlines(240)
		f09 = lj52.readlines(240)
		f10 = lj52.readlines(240)
		f11 = lj52.readlines(240)
		f12 = lj52.readlines(240)
		f13 = lj52.readlines(240)
		f14 = lj52.readlines(240)
		f15 = lj52.readlines(240)
		f16 = lj52.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 52 - 27 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)

def Loja53():

	try:
		with open("relver_loja53.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('101 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_102.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('102 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_103.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('103 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_104.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('104 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_105.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('105 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_106.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('106 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_107.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('107 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_108.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('108 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_109.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('109 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_110.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('110 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_111.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('111 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_112.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('112 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_113.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('113 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_114.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('114 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_115.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('115 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)
	try:
		with open("relver_loja53.txt", "a") as stream:
			for line in open('D:\REMARCA\lojas\lj53.verpdv_116.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja53.txt", "a") as stream:
						print('116 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                          ', file=stream)

	with open("relver_loja53.txt") as lj53:
		f01 = lj53.readlines(240)
		f02 = lj53.readlines(240)
		f03 = lj53.readlines(240)
		f04 = lj53.readlines(240)
		f05 = lj53.readlines(240)
		f06 = lj53.readlines(240)
		f07 = lj53.readlines(240)
		f08 = lj53.readlines(240)
		f09 = lj53.readlines(240)
		f10 = lj53.readlines(240)
		f11 = lj53.readlines(240)
		f12 = lj53.readlines(240)
		f13 = lj53.readlines(240)
		f14 = lj53.readlines(240)
		f15 = lj53.readlines(240)
		f16 = lj53.readlines(240)
		
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 53 - 16 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(NFC-e)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)
		listbox.insert(5, f02)
		listbox.insert(6, f03)
		listbox.insert(7, f04)
		listbox.insert(8, f05)
		listbox.insert(9, f06)
		listbox.insert(10, f07)
		listbox.insert(11, f08)
		listbox.insert(12, f09)
		listbox.insert(13, f10)
		listbox.insert(14, f11)
		listbox.insert(15, f12)
		listbox.insert(16, f13)
		listbox.insert(17, f14)
		listbox.insert(18, f15)
		listbox.insert(19, f16)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)


def Loja301():

	try:
		with open("relver_loja301.txt", "w") as stream:
			for line in open('D:\REMARCA\lojas\lj301.verpdv_101.txt'):
				print((line.rstrip()), file=stream)
	except FileNotFoundError:
				with open("relver_loja301.txt", "a") as stream:
						print('001 -  SEM CONEXÃO OU PDV COM DEFEITO                                                                                                                                                                                                                                             ', file=stream)

	with open("relver_loja301.txt") as lj301:
		f01 = lj301.readlines(240)
	
		scrollbar = tk.Scrollbar(gui, orient="vertical")
		listbox = tk.Listbox(gui, width=250, height=31, yscrollcommand=scrollbar.set, font=Font(family="Calibri", size=9))
		scrollbar.config(command=listbox.yview)
		scrollbar.place(x=10, y=250)
		
		listbox.focus()
		listbox.delete(0,END)

		listbox.insert(0, "LOJA 301 - 01 pdvs:")
		listbox.insert(1, " ")
		listbox.insert(2, "Caixa(SAT)")
		listbox.insert(3, " ")
		listbox.insert(4, f01)

		listbox.itemconfigure(0, fg="#ff0000", bg="#fff")
		
		listbox.place(x=0, y=250)
		
		listbox.selection_set(first=4)
		
		
btnSair = Button(bottomSair, text='Sair', bg="red", fg="yellow", width=10, height=1, font="Arial 10", command=gui.quit)
btnSair.bind('<Button-1>', Fim)
btnSair.pack()


gui.mainloop()
