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
user = 'NAGUMO\cpd_l01' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja1"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l02' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja2"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l03' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja3"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l04' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja4"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l06' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja6"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l07' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja7"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l08' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja8"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l09' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja9"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l10' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja10"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l11' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja11"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l12' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja12"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l13' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja13"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l14' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja14"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l15' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja15"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l16' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja16"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l17' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja17"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l18' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja18"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l19' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja19"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l20' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja20"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l21' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja21"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l22' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja22"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.23.101\C$' 
user = 'NAGUMO\cpd_l23' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja23"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.24.101\C$' 
user = 'NAGUMO\cpd_l24' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja24"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l25' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja25"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l26' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja26"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l27' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja27"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l28' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja28"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l29' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja29"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l30' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja30"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l31' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja31"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.32.101\C$' 
user = 'NAGUMO\cpd_l32' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja32"
for file in glob.glob(r'Y:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.33.101\C$' 
user = 'NAGUMO\cpd_l33' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja33"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l34' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja34"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l35' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja35"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l36' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja36"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l37' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja37"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l38' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja38"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l39' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja39"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l40' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja40"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l41' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja41"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l42' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja42"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l43' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja43"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l44' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja44"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l45' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja45"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l46' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja46"
for file in glob.glob(r'Q:/RETAG/*.INI'):
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
user = 'NAGUMO\cpd_l47' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja47"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.48.101\C$' 
user = 'NAGUMO\cpd_l48' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja48"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\10.132.49.101\C$' 
user = 'NAGUMO\cpd_l49' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja49"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')
# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.50.101\C$' 
user = 'NAGUMO\cpd_l50' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja50"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.51.101\C$' 
user = 'NAGUMO\cpd_l51' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja51"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.52.101\C$' 
user = 'NAGUMO\cpd_l52' 
password = 'retag@2019'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja52"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

# initialize
driveLetter = 'Q:' 
networkPath = '\\\\192.168.53.101\C$' 
user = 'NAGUMO\cpd_l53' 
password = 'retag@2018'

# Connect to map network drive to letter Q
winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Copiando arquivos para o Retag, aguarde....')
time.sleep(10)

os.chdir('C:\\')

dest_dir = "C:\\RETAG\CONF\loja53"
for file in glob.glob(r'Q:/RETAG/*.INI'):
	print(file)
	shutil.copy(file, dest_dir)

# Disconnect anything on drive letter Q
winCMD = 'NET USE ' + driveLetter + ' /delete'
print(winCMD)
subprocess.call(winCMD, shell=True)

print('Arquivos copiados com sucesso!')

print('---------------------------------------------------------')
input("Pressione ENTER para terminar!!!!")
