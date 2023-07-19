import six

from tkinter import Tk
from tkinter.filedialog import askopenfilename


janela_padrao = Tk().withdraw()
caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.log"), ("Arquivos csv", "*.txt")))


cartao = '0,2021'
retorno = '0,132'
bandeira = '0,156'

if caminho_do_arquivo:
	with open(caminho_do_arquivo, encoding='iso-8859-1') as arquivo:
		for linha in arquivo:
			if (bandeira in linha) or (retorno in linha) or (cartao in linha):
				print(linha, end='')
			
else:	
    print("Nenhum arquivo selecionado")


six.moves.input( 'Pressione <ENTER> para sair...' )

