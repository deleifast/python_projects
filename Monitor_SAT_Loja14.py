#encoding: iso-8859-1
import subprocess, os, sys


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.5 ""c:\\pdv\inicia_sat.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj14.txt', 'a') as caixa:
		caixa.write('SAT não reiniciado\n')
		caixa.close()
else:
	print("SAT iniciado_Caixa 05")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.7 ""c:\\pdv\inicia_sat.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj14.txt', 'a') as caixa:
		caixa.write('SAT não reiniciado\n')
		caixa.close()
else:
	print("SAT iniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\inicia_sat.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11Lj14.txt', 'a') as caixa:
		caixa.write('SAT não reiniciado\n')
		caixa.close()
else:
	print("SAT iniciado_Caixa 07")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")


