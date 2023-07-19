#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path
from pathlib import Path


# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.3.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.3.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')


# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.4.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.4.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.6.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.6.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.7.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.7.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.8.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.8.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.9.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.9.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.10.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.10.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.11.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.11.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.12.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.12.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.13.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.13.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')


# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.141.150\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.141.150 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.15.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.15.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.16.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.16.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.17.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.17.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.18.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.18.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')


# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.19.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.19.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.20.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.20.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.21.100\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.21.100 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.22.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.22.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.24.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.24.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.25.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.25.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.26.150\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.26.150 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.27.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.27.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.28.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.28.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.29.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.29.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.30.102\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.30.102 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.32.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.32.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.33.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.33.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.34.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.34.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.35.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.35.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.36.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.37.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.37.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.38.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.38.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.39.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.39.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.40.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.40.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.42.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.42.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.43.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.43.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.44.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.44.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.45.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.45.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.46.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.46.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.47.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.47.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.48.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 192.168.48.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')


# initialize
driveLetter = 'Q:' 
networkPath = '\\\\10.132.49.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

os.chdir('Q:\\')

if os.path.exists("Q:\\FielRetag"):
	print ('existe FIELRETAG')
else:
	dir = './FielRetag'
	os.makedirs(dir)

if os.path.exists("Q:\\Retag\PLAY"):
	print ('existe RETAG\PLAY')
else:
	dir = './Retag/PLAY'
	os.makedirs(dir)

os.remove('Q:/FielRetag/FielRetag.ini')

os.chdir('C:\\ATUAL')

with open("FielRetag.ini","a") as PRINI:
	item = input("Digite [CONFIG]:")
	item1 = input("Digite LOJA = o número da loja:")
	PRINI.write("%s \n" % item+item1)

os.chdir('C:\\ATUAL')

arquivo = open("C:\\ATUAL\FielRetag.ini","a") 
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('[URL]\n')
arquivo.write('CONSULTA=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('OFERTAS=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php\n')
arquivo.write('ENVIO=http://www.dashboard-magictv.com.br/nagumoplay/webservices/bonificacao_pontos/tratarjson.php')
arquivo.write('\n')
arquivo.write('\n')
arquivo.close()

arquivo1 = open("C:\\ATUAL\FielSender.ini","a")
arquivo1.write('[PASTA]\n')
arquivo1.write('NP=C:\PDV\RX')
arquivo1.write('\n')
arquivo1.write('MOVENP=C:\RETAG\PLAY')
arquivo1.write('\n')
arquivo1.close()

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.ini'):
	print(file)
	shutil.copy(file, dest_dir)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielSender.ini'):
	print(file)
	shutil.copy(file, dest_dir)

os.remove('C:\\ATUAL\FielRetag.ini')

os.system("taskkill /s 10.132.49.101 /u compartilhar /p ruaf305 /im FielRetag.exe")
os.rename('Q://FielRetag/FielRetag.exe','Q://FielRetag/FielRetag.140318')

print('Copiando arquivos para o FielRetag, aguarde....')
time.sleep(10)

dest_dir = "Q:\\FielRetag"
for file in glob.glob(r'C:/Atual/FielRetag.exe'):
	print(file)
	shutil.copy(file, dest_dir)

os.chdir('C:\\ATUAL')

print ("Diretorio atual: %s" % os.getcwd())

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')


input("Pressione ENTER para terminar")