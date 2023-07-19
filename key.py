from subprocess import call
from os import path

if path.exists('produkey.exe'):
	key = 'produkey.exe /IEKeys 0 /OfficeKeys 0 /SQLKeys 0 /ExchangeKeys 0 /ExtractEdition 0 /stab key.txt'
	call(key)

else:
	with open("key.txt", "w") as stream:
		print('PRODUKEY.EXE NÃO EXISTE, VERIFICAR!', file=stream)


