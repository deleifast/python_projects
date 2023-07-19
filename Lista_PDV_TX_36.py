#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, sys, os.path, socket
from pathlib import Path


# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.1\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx01_lj36.txt":
				os.remove(file)

		with open('pdv_cx01_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 01")

		os.chdir("Q://PDV/TX")
		
		pastas = os.listdir()
		total = 0
		arq = open("C://PDV/lista_de_arquivos_cx01.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
			
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.2\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx02_lj36.txt":
				os.remove(file)

		with open('pdv_cx02_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 02")


		os.chdir("Q://PDV/TX")
		
		pastas = os.listdir()
		total = 0
		arq = open("C://PDV/lista_de_arquivos_cx02.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()
			time.sleep(5)
			
			# Desconectando drive Q
			winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
			print(winCMD)
			subprocess.call(winCMD, shell=True)
			os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.3\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx03_lj36.txt":
				os.remove(file)

		with open('pdv_cx02_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 03")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx03.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.4\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx04_lj36.txt":
				os.remove(file)

		with open('pdv_cx04_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 04")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx04.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.5\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx05_lj36.txt":
				os.remove(file)

		with open('pdv_cx05_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 05")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx05.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.6\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx06_lj36.txt":
				os.remove(file)

		with open('pdv_cx06_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 06")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx06.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.7\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx07_lj36.txt":
				os.remove(file)

		with open('pdv_cx07_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 07")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx07.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.8\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx08_lj36.txt":
				os.remove(file)

		with open('pdv_cx08_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 08")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx08.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.9\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx09_lj36.txt":
				os.remove(file)

		with open('pdv_cx09_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 09")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx09.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.10\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx10_lj36.txt":
				os.remove(file)

		with open('pdv_cx10_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 10")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx10.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.11\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx11_lj36.txt":
				os.remove(file)

		with open('pdv_cx11_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 11")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx11.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.12\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx12_lj36.txt":
				os.remove(file)

		with open('pdv_cx12_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 12")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx12.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.13\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx13_lj36.txt":
				os.remove(file)

		with open('pdv_cx13_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 13")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx13.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.14\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx14_lj36.txt":
				os.remove(file)

		with open('pdv_cx14_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 14")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx14.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.15\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx15_lj36.txt":
				os.remove(file)

		with open('pdv_cx15_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 15")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx15.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.16\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx16_lj36.txt":
				os.remove(file)

		with open('pdv_cx16_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 16")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx16.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.17\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx17_lj36.txt":
				os.remove(file)

		with open('pdv_cx17_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 17")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx17.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")

# Mapeando drive de rede
driveLetter = 'Q:' 
networkPath = '\\\\192.168.36.18\C$' 
user = 'pdv' 
password = 'pdv'

winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
exitcode = subprocess.call(winCMD, shell=True)
print (exitcode)

if exitcode == 2:
	
		exitcode == 2

		os.chdir('C:\\Atual')

		path = 'C:\\Atual'
		dir = os.listdir(path)
		for file in dir:
			if file == "pdv_cx18_lj36.txt":
				os.remove(file)

		with open('pdv_cx18_lj36.txt', 'a') as caixa:
			caixa.write('PDV não listado')
			caixa.close()


else:
		exitcode == 0
		print("Conectado Caixa 18")


		os.chdir('Q:\\PDV\TX')

		pastas = os.listdir()
		total = 0
		arq = open("c://pdv/lista_de_arquivos_cx18.txt", "w",encoding="utf-8")
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
			arq.write("# Total de arquivos : "+ str(total))
			arq.close()		
		
		# Desconectando drive Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /yes'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		os.chdir("C://")
