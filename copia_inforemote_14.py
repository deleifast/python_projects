#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path, socket, datetime
from pathlib import Path
from datetime import datetime


# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.1\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx01_lj14.txt":
				os.remove(file)

		with open('pdv_cx01_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 01")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx101"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.2\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx02_lj14.txt":
				os.remove(file)

		with open('pdv_cx02_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 02")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx102"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
			
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.3\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx03_lj14.txt":
				os.remove(file)

		with open('pdv_cx03_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 03")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx103"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.4\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx04_lj14.txt":
				os.remove(file)

		with open('pdv_cx04_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 04")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx104"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.5\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx05_lj14.txt":
				os.remove(file)

		with open('pdv_cx05_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 05")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx105"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.6\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx06_lj14.txt":
				os.remove(file)

		with open('pdv_cx06_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 06")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx106"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.7\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx07_lj14.txt":
				os.remove(file)

		with open('pdv_cx07_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 07")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx107"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.8\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx08_lj14.txt":
				os.remove(file)

		with open('pdv_cx08_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 08")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx108"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.9\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx09_lj14.txt":
				os.remove(file)

		with open('pdv_cx09_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 09")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx109"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.10\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx010_lj14.txt":
				os.remove(file)

		with open('pdv_cx010_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 10")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx110"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.11\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx011_lj14.txt":
				os.remove(file)

		with open('pdv_cx011_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 11")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx111"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.12\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx012_lj14.txt":
				os.remove(file)

		with open('pdv_cx012_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 12")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx112"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.13\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx013_lj14.txt":
				os.remove(file)

		with open('pdv_cx013_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 13")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx113"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.14\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx014_lj14.txt":
				os.remove(file)

		with open('pdv_cx014_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 14")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx114"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.15\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Remarca')

		path = 'C:\\Remarca'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx015_lj14.txt":
				os.remove(file)

		with open('pdv_cx015_lj14.txt', 'a') as caixa:
			caixa.write('INFO não copiado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 15")

		os.chdir('C:\\REMARCA')

		print('Copiando INFOR24.TXT, aguarde....')
		time.sleep(5)

		dest_dir = "C:\\REMARCA\loja14\cx115"
		for file in glob.glob(r'Q://LOG/INFOR24.TXT'):
			shutil.copy(file, dest_dir)
			print(file)
		
		else:
			print('INFO não encontrado')
		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
