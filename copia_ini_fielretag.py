import os
import shutil
import subprocess 
import time
import glob
import copy
import sys

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.1.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja1"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.2.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja2"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.3.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja3"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja4"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja6"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja7"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja8"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja9"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja10"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja11"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja12"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja13"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja14"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja15"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja16"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja17"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja18"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja19"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja20"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja21"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja22"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
#driveLetter = 'Q:' 
#networkPath = '\\\\192.168.23.101\C$' 
#user = 'compartilhar' 
#password = 'ruaf305'

# Connect to map network drive to letter Q
#winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Copiando arquivos para o FIELRETAG, aguarde....')
#time.sleep(10)

#os.chdir('C:\\')

#dest_dir = "C:\\RETAG\CONF\loja23"
#for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
#	print(file)
#	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
#winCMD = 'NET USE ' + driveLetter + ' /delete'
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.24.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja24"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja25"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja26"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja27"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja28"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja29"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja30"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.31.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja31"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
#driveLetter = 'Q:' 
#networkPath = '\\\\192.168.32.101\C$' 
#user = 'compartilhar' 
#password = 'ruaf305'

# Connect to map network drive to letter Q
#winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Copiando arquivos para o FIELRETAG, aguarde....')
#time.sleep(10)

#os.chdir('C:\\')

#dest_dir = "C:\\RETAG\CONF\loja32"
#for file in glob.glob(r'Y:/FIELRETAG/*.INI'):
#	print(file)
#	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
#winCMD = 'NET USE ' + driveLetter + ' /delete'
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.33.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja33"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja34"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja35"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja36"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja37"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja38"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja39"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja40"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.41.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja41"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja42"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja43"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja44"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja45"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja46"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
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

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja47"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
#driveLetter = 'Q:' 
#networkPath = '\\\\192.168.48.101\C$' 
#user = 'compartilhar' 
#password = 'ruaf305'

# Connect to map network drive to letter Q
#winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Copiando arquivos para o FIELRETAG, aguarde....')
#time.sleep(10)

#os.chdir('C:\\')

#dest_dir = "C:\\RETAG\CONF\loja48"
#for file in glob.glob(r'Z:/FIELRETAG/*.INI'):
#	print(file)
#	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
#winCMD = 'NET USE ' + driveLetter + ' /delete'
#print(winCMD)
#subprocess.call(winCMD, shell=True)

#print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\10.132.49.101\C$' 
user = 'compartilhar' 
password = 'ruaf305'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o FIELRETAG, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja49"
for file in glob.glob(r'Q:/FIELRETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

print('NAO ESQUECER DE VERIFICAR AS LOJAS - 23 / 32 / 48!!!!')
print('---------------------------------------------------------')
print('---------------------------------------------------------')
input("Pressione ENTER para terminar!!!!")
