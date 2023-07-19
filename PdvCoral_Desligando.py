#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, copy, os.path, sys, socket

from datetime import datetime

os.chdir('C:\\PDV')

path = 'C:\\PDV'
dir = os.listdir(path)
for file in dir:
	if file == "pdv_desligado.txt":
		os.remove(file)

today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute

hostName    = ""

ipAddress   = socket.gethostbyname_ex(socket.gethostname())

with open('pdv_desligado.txt', 'a') as caixa:
	caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
	caixa.write(str(" dia "))
	caixa.write(str(day))
	caixa.write(str("/"))
	caixa.write(str(month))
	caixa.write(str("/"))
	caixa.write(str(year))
	caixa.write("   às   ")
	caixa.write(str(hour))
	caixa.write(str(" hora(s)"))
	caixa.write(str(" e "))
	caixa.write(str(minute))
	caixa.write(str(" minuto(s)"))
	caixa.close()

		
os.startfile(r"Enviando_Email_Desliga.exe")

time.sleep(10)

sys.exit()


