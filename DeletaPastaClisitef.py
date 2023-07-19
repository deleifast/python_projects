#encoding: iso-8859-1
import os, time, subprocess, shutil, os.path, sys, glob

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.12\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa01")
	else:
		print ("Pasta não existe Caixa01")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa01lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /DELETE '
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.13\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa02")
	else:
		print ("Pasta não existe Caixa02")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa02lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /DELETE'
subprocess.call(winCMD, shell=True)

time.sleep(5)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.14\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa03")
	else:
		print ("Pasta não existe Caixa03")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa03lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /DELETE'
subprocess.call(winCMD, shell=True)

time.sleep(5)

'''
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.4\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa04")
	else:
		print ("Pasta não existe Caixa04")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa04lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.5\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa05")
	else:
		print ("Pasta não existe Caixa05")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa05lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.6\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa06")
	else:
		print ("Pasta não existe Caixa06")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa06lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.7\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa07")
	else:
		print ("Pasta não existe Caixa07")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa07lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.8\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa08")
	else:
		print ("Pasta não existe Caixa08")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa08lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.9\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa09")
	else:
		print ("Pasta não existe Caixa09")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa09lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.10\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa10")
	else:
		print ("Pasta não existe Caixa10")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa10lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.11\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa11")
	else:
		print ("Pasta não existe Caixa11")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa11lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.12\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa12")
	else:
		print ("Pasta não existe Caixa12")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa12lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.13\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa13")
	else:
		print ("Pasta não existe Caixa13")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa13lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.14\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa14")
	else:
		print ("Pasta não existe Caixa14")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa14lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)

time.sleep(10)

driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.15\C$' 
user = 'pdv' 
password = 'pdv'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)

if exitcode == 0:
	os.chdir('Q:\\')
	if os.path.exists("Q:\CliSitef"):
		shutil.rmtree('/CliSitef/')
		print("Pasta agapada_Caixa15")
	else:
		print ("Pasta não existe Caixa15")	

else:
	exitcode == 2
	os.chdir('C:\\ATUAL')
	with open('Caixa15lj14.txt', 'a') as caixa:
		caixa.write('Pasta não apagada\n')
		caixa.close()

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
subprocess.call(winCMD, shell=True)
'''