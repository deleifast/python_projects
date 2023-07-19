#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path, socket
from pathlib import Path


# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.1.101\C$' 
user = 'cpd_l01' 
password = 'retag@2018'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "retag_lj01.txt":
				os.remove(file)

		with open('retag_lj01.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Retag lj01")

		os.chdir("Q://RemarcaDN")
		
		pastas = os.listdir()
		total = 0
		arq = open("C://PDV/lista_DN_LJ01.txt", "w",encoding="utf-8")
		def listar_pasta(pasta):
			tot = 0
			subpastas = list()
			if os.path.isdir(pasta):
				items = os.listdir(pasta)
				print("\n\nARQUIVOS NA PASTA '"+ str(pasta).upper() + "' :",end='\n\n')
				arq.write("ARQUIVOS NA PASTA '"+ str(pasta).upper() +"': \n")
				for item in items:
					novo_item = os.path.join(pasta,item)
					if os.path.isdir(novo_item):
						subpastas.append(novo_item)
						continue
					print(item)
					arq.write(item + "\n")
					tot += 1
				for subpasta in subpastas:
					tot += listar_pasta(subpasta)
			arq.write("\n")
			return tot

		if __name__ == '__main__':
			for pasta in pastas:
				total +=  listar_pasta(pasta)
			print("Total de arquivos: " + str(total))
			arq.write("Total de arquivos : "+ str(total))
			arq.close()		
			
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

