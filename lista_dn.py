#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path, socket, datetime
from pathlib import Path
from datetime import datetime

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

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "caixa01.txt":
				os.remove(file)

		with open('caixa01.txt', 'a') as caixa:
			caixa.write('XML não copiado')
			caixa.close()


else:
		exitcode == 0

		try:
							
			caminho = r'Q:/RemarcaDN/'		
		
			res = (caminho)
			print (res)
			
			filenames = []

			for filename in os.listdir(res):
				if not filename.startswith('DN'):
					continue
				fullname = os.path.join(filename)
				print(fullname)
				filenames.append(fullname)

				
		except FileNotFoundError:
				print()
				print('Não existe essa data para esse PDV')
				print()

		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
