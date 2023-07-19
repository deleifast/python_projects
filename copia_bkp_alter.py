#encoding: iso-8859-1

import os, shutil, glob, sys, os.path
from pathlib import Path

os.chdir('C:\\bkpalter')

path = 'C:\\bkpalter'
dir = os.listdir(path)
for file in dir:
	if file.startswith('R'):
		os.remove(file)
		print('Arquivos deletados')

dest_dir = "C:\\bkpalter"
for file in glob.glob(r'C:\\Program Files (x86)\\Alterdata\\Backup\\*.Zip'):
	shutil.copy(file, dest_dir)

		
