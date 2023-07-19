#coding: utf-8


import rarfile

rarpath='c:\pdv\loja14_pdv.rar'

def unrar(file):
    rf=rarfile.RarFile(file)
    rf.extractall()

unrar(rarpath)

print('Pronto pdv!' + '\n')



