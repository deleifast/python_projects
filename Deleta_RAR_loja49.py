#encoding: iso-8859-1

import os, glob, subprocess


# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.1\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx01_lj49.txt":
				os.remove(file)

		with open('pdv_cx01_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 01")

	os.chdir('Q:\\PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:\\PDV\\PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.2\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx02_lj49.txt":
				os.remove(file)

		with open('pdv_cx02_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 02")

	os.chdir('Q:\\PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:\\PDV\\PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.3\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx03_lj49.txt":
				os.remove(file)

		with open('pdv_cx03_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 03")


	os.chdir('Q://PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.4\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx04_lj49.txt":
				os.remove(file)

		with open('pdv_cx04_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 04")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.5\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx05_lj49.txt":
				os.remove(file)

		with open('pdv_cx05_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 05")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.6\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx06_lj49.txt":
				os.remove(file)

		with open('pdv_cx06_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 06")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.7\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx07_lj49.txt":
				os.remove(file)

		with open('pdv_cx07_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 07")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.8\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx08_lj49.txt":
				os.remove(file)

		with open('pdv_cx08_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 08")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.9\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx09_lj49.txt":
				os.remove(file)

		with open('pdv_cx09_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 09")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.10\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx10_lj49.txt":
				os.remove(file)

		with open('pdv_cx10_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 10")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.11\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx11_lj49.txt":
				os.remove(file)

		with open('pdv_cx11_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 11")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.12\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx12_lj49.txt":
				os.remove(file)

		with open('pdv_cx12_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 12")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.13\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx13_lj49.txt":
				os.remove(file)

		with open('pdv_cx13_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 13")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.14\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx14_lj49.txt":
				os.remove(file)

		with open('pdv_cx14_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 14")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.15\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx15_lj49.txt":
				os.remove(file)

		with open('pdv_cx15_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 15")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.16\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx16_lj49.txt":
				os.remove(file)

		with open('pdv_cx16_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 16")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.17\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx17_lj49.txt":
				os.remove(file)

		with open('pdv_cx17_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 17")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.18\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx18_lj49.txt":
				os.remove(file)

		with open('pdv_cx18_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 18")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.19\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx19_lj49.txt":
				os.remove(file)

		with open('pdv_cx19_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 19")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.20\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx20_lj49.txt":
				os.remove(file)

		with open('pdv_cx20_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 20")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.21\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx21_lj49.txt":
				os.remove(file)

		with open('pdv_cx21_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 21")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.22\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx22_lj49.txt":
				os.remove(file)

		with open('pdv_cx22_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 22")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)
# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.23\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx23_lj49.txt":
				os.remove(file)

		with open('pdv_cx23_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 23")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.24\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx24_lj49.txt":
				os.remove(file)

		with open('pdv_cx24_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 24")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.25\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx25_lj49.txt":
				os.remove(file)

		with open('pdv_cx25_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 25")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.26\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx26_lj49.txt":
				os.remove(file)

		with open('pdv_cx26_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 26")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\10.133.49.27\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\PDV')

		path = 'C:\\PDV'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx27_lj49.txt":
				os.remove(file)

		with open('pdv_cx27_lj49.txt', 'a') as caixa:
			caixa.write('PdvCoral-loja49 não alterado')
			caixa.close()


else:
	exitcode == 0
	print("Conectado Caixa 27")

	current_directory = os.path.dirname(os.path.abspath(__file__))

	os.chdir('Q:/PDV')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	os.chdir('Q:/PDV/PLUGIN')

	files = glob.glob('*.rar')
	for file in files:
		os.remove(file)

	# Desconectando drive Q
	winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
	print(winCMD)
	subprocess.call(winCMD, shell=True)
