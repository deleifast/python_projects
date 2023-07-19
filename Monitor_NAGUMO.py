#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor = W)

gui.title("MONITOR PASTA MATRIZ - NAGUMO")
gui.geometry("600x250")
gui.resizable(0,0)

load = Image.open("logo_2016.png")
render = ImageTk.PhotoImage(load)
img= Label(gui, image=render)
img.image = render
img.place(x=365, y=0)

def sel():
   selection = "ESCOLHIDA OPÇÃO: " + str(var.get()) + " DO MENU!!!"
   label.config(text = selection, font="Terminal 12")
   label.place(x=10, y=50)

var= IntVar()

R1 = Radiobutton(gui, text="1 - Monitorar PDV", variable=var, value=1, font="Arial 10", command=sel)
R1.pack( anchor = NW )

R2 = Radiobutton(gui, text="2 - Reiniciar SALTRANS", variable=var, value=2, font="Arial 10", command=sel)
R2.pack( anchor = NW )

mensagem= StringVar()
lbl = Label(gui, text="Remarca - telefone: (11)2755-7911 " , fg="red", font="Arial 15")
lbl.place(x=140, y=220)

mensagem= StringVar()
lbl = Label(gui, text="Versão 1.0" , fg="black", font="Arial 8")
lbl.place(x=1, y=230)
#Versão 2.0 - Alteração - tirado pdvcoral.exe e colocado inicia_pdv.bat

label = Label(gui)
label.pack()

def Loja01():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITORMONITOR')

		os.startfile(r"monitor_lj01.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.1.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.1.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja02():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj02.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.2.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.2.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja03():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj03.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.3.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.3.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja04():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj04.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.4.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.4.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja06():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj06.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.6.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.6.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja07():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj07.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.7.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.7.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja08():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj08.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.8.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.8.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja09():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj09.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.9.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.9.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja10():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj10.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.10.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.10.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja11():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj11.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.11.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.11.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja12():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj12.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.12.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.12.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja13():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj13.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.13.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
			
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.13.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	

def Loja14():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj14.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.141.150 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.141.150 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja15():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj15.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.15.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.15.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja16():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj16.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.16.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.16.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja17():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj17.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.17.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.17.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja18():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj18.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.18.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.18.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja19():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj19.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.19.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.19.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja20():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj20.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.20.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.20.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja21():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj21.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.21.100 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.21.100 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja22():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj22.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.22.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.22.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja23():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj23.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.23.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.23.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja24():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj24.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.24.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.24.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja25():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj25.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.25.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.25.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja26():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj26.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.26.150 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.26.150 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja27():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj27.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.27.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.27.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja28():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj28.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.28.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.28.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja29():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj29.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.29.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.29.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja30():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj30.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.30.102 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.30.102 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja31():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj31.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.31.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.31.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja32():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj32.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.32.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.32.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja33():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj33.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.33.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.33.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja34():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj34.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.34.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.34.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja35():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj35.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.35.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.35.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja36():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj36.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.36.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.36.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja37():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj37.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.37.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.37.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja38():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj38.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.38.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.38.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja39():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj39.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.39.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.39.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja40():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj40.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.40.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.40.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja41():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj41.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.41.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.41.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja42():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj42.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.42.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.42.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja43():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj43.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.43.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.43.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja44():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj44.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.44.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.44.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja45():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj45.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.45.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.45.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja46():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj46.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.46.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.46.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja47():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj47.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.47.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.47.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja48():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj48.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 192.168.48.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.48.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	

def Loja49():
	if var.get() == 1:
		os.chdir('C:\\ATUAL\MONITOR')

		os.startfile(r"monitor_lj49.exe")
	
	elif var.get() == 2:
			subprocess.call("taskkill /s 10.132.49.101 /u compartilhar /p ruaf305 /im Saltrans.exe", shell=True)
		
			ret = subprocess.call("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\10.132.49.101 ""c:\\Saltrans\Saltrans.exe", shell=True)
			if ret ==2:
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			elif ret == 53:
				resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			elif ret == 1326:
				resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			else:
				resp = messagebox.showinfo("Informação", "Saltrans Reiniciado!")
	else:
		resp = messagebox.showwarning("Alerta", "1 - MONITORAR MATRIZ  OU  2 - REINICIAR SALTRANS!")	
	





btn1 = Button(bottomFrame, text="Loja 01", bg="white", fg="black", command=Loja01)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn1.bind('<Button-1>')
btn1.grid(column=0, row = 1)

btn2 = Button(bottomFrame, text="Loja 02", bg="white", fg="black", command=Loja02)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn2.bind('<Button-1>')
btn2.grid(column=1, row = 1)

btn3 = Button(bottomFrame, text="Loja 03", bg="white", fg="black", command=Loja03)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn3.bind('<Button-1>')
btn3.grid(column=2, row = 1)

btn4 = Button(bottomFrame, text="Loja 04", bg="white", fg="black", command=Loja04)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn4.bind('<Button-1>')
btn4.grid(column=3, row = 1)

btn6 = Button(bottomFrame, text="Loja 06", bg="white", fg="black", command=Loja06)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn6.bind('<Button-1>')
btn6.grid(column=4, row = 1)

btn7 = Button(bottomFrame, text="Loja 07", bg="white", fg="black", command=Loja07)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn7.bind('<Button-1>')
btn7.grid(column=5, row = 1)

btn8 = Button(bottomFrame, text="Loja 08", bg="white", fg="black", command=Loja08)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn8.bind('<Button-1>')
btn8.grid(column=6, row = 1)

btn9 = Button(bottomFrame, text="Loja 09", bg="white", fg="black", command=Loja09)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn9.bind('<Button-1>')
btn9.grid(column=7, row = 1)

btn10 = Button(bottomFrame, text="Loja 10", bg="white", fg="black", command=Loja10)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn10.bind('<Button-1>')
btn10.grid(column=8, row = 1)

btn11 = Button(bottomFrame, text="Loja 11", bg="white", fg="black", command=Loja11)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn11.bind('<Button-1>')
btn11.grid(column=9, row = 1)

btn12 = Button(bottomFrame, text="Loja 12", bg="white", fg="black", command=Loja12)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn12.bind('<Button-1>')
btn12.grid(column=10, row = 1)

btn13 = Button(bottomFrame, text="Loja 13", bg="white", fg="black", command=Loja13)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn13.bind('<Button-1>')
btn13.grid(column=11, row = 1)

btn14 = Button(bottomFrame, text="Loja 14", bg="white", fg="black", command=Loja14)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn14.bind('<Button-1>')
btn14.grid(column=0, row = 2)

btn15 = Button(bottomFrame, text="Loja 15", bg="white", fg="black", command=Loja15)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn15.bind('<Button-1>')
btn15.grid(column=1, row = 2)

btn16 = Button(bottomFrame, text="Loja 16", bg="white", fg="black", command=Loja16)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn16.bind('<Button-1>')
btn16.grid(column=2, row = 2)

btn17 = Button(bottomFrame, text="Loja 17", bg="white", fg="black", command=Loja17)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn17.bind('<Button-1>')
btn17.grid(column=3, row = 2)

btn18 = Button(bottomFrame, text="Loja 18", bg="white", fg="black", command=Loja18)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn18.bind('<Button-1>')
btn18.grid(column=4, row = 2)

btn19 = Button(bottomFrame, text="Loja 19", bg="white", fg="black", command=Loja19)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn19.bind('<Button-1>')
btn19.grid(column=5, row = 2)

btn20 = Button(bottomFrame, text="Loja 20", bg="white", fg="black", command=Loja20)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn20.bind('<Button-1>')
btn20.grid(column=6, row = 2)

btn21 = Button(bottomFrame, text="Loja 21", bg="white", fg="black", command=Loja21)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn21.bind('<Button-1>')
btn21.grid(column=7, row = 2)

btn22 = Button(bottomFrame, text="Loja 22", bg="white", fg="black", command=Loja22)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn22.bind('<Button-1>')
btn22.grid(column=8, row = 2)

btn23 = Button(bottomFrame, text="Loja 23", bg="white", fg="black", command=Loja23)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn23.bind('<Button-1>')
btn23.grid(column=9, row = 2)

btn24 = Button(bottomFrame, text="Loja 24", bg="white", fg="black", command=Loja24)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn24.bind('<Button-1>')
btn24.grid(column=10, row = 2)

btn25 = Button(bottomFrame, text="Loja 25", bg="white", fg="black", command=Loja25)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn25.bind('<Button-1>')
btn25.grid(column=11, row = 2)

btn26 = Button(bottomFrame, text="Loja 26", bg="white", fg="black", command=Loja26)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn26.bind('<Button-1>')
btn26.grid(column=0, row = 3)

btn27 = Button(bottomFrame, text="Loja 27", bg="white", fg="black", command=Loja27)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn27.bind('<Button-1>')
btn27.grid(column=1, row = 3)

btn28 = Button(bottomFrame, text="Loja 28", bg="white", fg="black", command=Loja28)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn28.bind('<Button-1>')
btn28.grid(column=2, row = 3)

btn29 = Button(bottomFrame, text="Loja 29", bg="white", fg="black", command=Loja29)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn29.bind('<Button-1>')
btn29.grid(column=3, row = 3)

btn30 = Button(bottomFrame, text="Loja 30", bg="white", fg="black", command=Loja30)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn30.bind('<Button-1>')
btn30.grid(column=4, row = 3)

btn31 = Button(bottomFrame, text="Loja 31", bg="white", fg="black", command=Loja31)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn31.bind('<Button-1>')
btn31.grid(column=5, row = 3)

btn32 = Button(bottomFrame, text="Loja 32", bg="white", fg="black", command=Loja32)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn32.bind('<Button-1>')
btn32.grid(column=6, row = 3)

btn33 = Button(bottomFrame, text="Loja 33", bg="white", fg="black", command=Loja33)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn33.bind('<Button-1>')
btn33.grid(column=7, row = 3)

btn34 = Button(bottomFrame, text="Loja 34", bg="white", fg="black", command=Loja34)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn34.bind('<Button-1>')
btn34.grid(column=8, row = 3)

btn35 = Button(bottomFrame, text="Loja 35", bg="white", fg="black", command=Loja35)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn35.bind('<Button-1>')
btn35.grid(column=9, row = 3)

btn36 = Button(bottomFrame, text="Loja 36", bg="white", fg="black", command=Loja36)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn36.bind('<Button-1>')
btn36.grid(column=10, row = 3)

btn37 = Button(bottomFrame, text="Loja 37", bg="white", fg="black", command=Loja37)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn37.bind('<Button-1>')
btn37.grid(column=11, row = 3)

btn38 = Button(bottomFrame, text="Loja 38", bg="white", fg="black", command=Loja38)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn38.bind('<Button-1>')
btn38.grid(column=0, row = 4)

btn39 = Button(bottomFrame, text="Loja 39", bg="white", fg="black", command=Loja39)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn39.bind('<Button-1>')
btn39.grid(column=1, row = 4)

btn40 = Button(bottomFrame, text="Loja 40", bg="white", fg="black", command=Loja40)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn40.bind('<Button-1>')
btn40.grid(column=2, row = 4)

btn41 = Button(bottomFrame, text="Loja 41", bg="white", fg="black", command=Loja41)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn41.bind('<Button-1>')
btn41.grid(column=3, row = 4)

btn42 = Button(bottomFrame, text="Loja 42", bg="white", fg="black", command=Loja42)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn42.bind('<Button-1>')
btn42.grid(column=4, row = 4)

btn43 = Button(bottomFrame, text="Loja 43", bg="white", fg="black", command=Loja43)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn43.bind('<Button-1>')
btn43.grid(column=5, row = 4)

btn44 = Button(bottomFrame, text="Loja 44", bg="white", fg="black", command=Loja44)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn44.bind('<Button-1>')
btn44.grid(column=6, row = 4)

btn45 = Button(bottomFrame, text="Loja 45", bg="white", fg="black", command=Loja45)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn45.bind('<Button-1>')
btn45.grid(column=7, row = 4)

btn46 = Button(bottomFrame, text="Loja 46", bg="white", fg="black", command=Loja46)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn46.bind('<Button-1>')
btn46.grid(column=8, row = 4)

btn47 = Button(bottomFrame, text="Loja 47", bg="white", fg="black", command=Loja47)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn47.bind('<Button-1>')
btn47.grid(column=9, row = 4)

btn48 = Button(bottomFrame, text="Loja 48", bg="white", fg="black", command=Loja48)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn48.bind('<Button-1>')
btn48.grid(column=10, row = 4)

btn49 = Button(bottomFrame, text="Loja 49", bg="white", fg="black", command=Loja49)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn49.bind('<Button-1>')
btn49.grid(column=11, row = 4)



btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=gui.quit)
#btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row = 5)


gui.mainloop()