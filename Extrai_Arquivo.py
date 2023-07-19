#coding: utf-8
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, tqdm
from zipfile import ZipFile

# specifying the zip file name
file_pdv = "c:\\pdv\pdv.zip"
 
with ZipFile(file_pdv) as zf:
	for member in tqdm(zf.infolist(), desc='Extracting '):
		try:
			zf.extract(member, 'c:\\teste')
		except zipfile.error as e:
			pass
'''
# opening the zip file in READ mode
with ZipFile(file_pdv, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
 
    # extracting all the files
    print('Extraindo todos os arquivos agora...')
    zip.extractall('c:\\pdv')
    print('Pronto pdv!' + '\n')

# specifying the zip file name
file_plugin = "c:\\pdv\plugin\plugin.zip"
 
# opening the zip file in READ mode
with ZipFile(file_plugin, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
 
    # extracting all the files
    print('Extraindo todos os arquivos agora...')
    zip.extractall('c:\\pdv\plugin')
    print('Pronto plugin!' + '\n')
'''