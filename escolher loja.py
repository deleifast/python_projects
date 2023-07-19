import os
import shutil

pasta = 'C://PDV/PRINI'
arquivo = str(input('digite o nome do arquivo que deseja copiar: '))
diretorio = os.listdir(pasta)
dest_dir = str(input('digite o nome da pasta que deseja copiar: '))

shutil.copy(arquivo, dest_dir)
print('%s copiado da pasta %s' % (arquivo, pasta))
exit()