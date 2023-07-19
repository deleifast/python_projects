import xml.etree.ElementTree as ET
import os, glob, os.path
from pathlib import Path

#XML = ("NFe33210815347973000179651110002182329001381307_procNFe.XML").strip('"')
#tree = ET.parse(XML)
#root = tree.getroot()
#print('\n')
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
path = "\pdv\\nfce"
#path = input("Digite a pasta: ")


filenames = []

for filename in os.listdir(path):
    if not filename.endswith('.XML'):
        continue
    fullname = os.path.join(path,filename)
    print(fullname)
    filenames.append(fullname)

with open("rel_xml.txt", 'w') as arquivo:
				
	for filename in filenames:
		with open(filename, 'r', encoding="utf-8") as content:
			tree = ET.parse(content)
			root = tree.getroot()

			for nf in root.findall('.//nfe:ide', ns):
				nota = nf.find('.//nfe:nNF', ns).text
				data = nf.find('.//nfe:dhEmi', ns).text
				serie = nf.find('.//nfe:serie', ns).text

			for m in root.findall('.//nfe:infProt', ns):
				motivo = m.find('.//nfe:xMotivo', ns).text

			for det in root.findall('.//nfe:pag', ns):
				tpag = det.find('.//nfe:tPag', ns).text
									
			
				if tpag == '01':
					print (f"Série: {serie}, Nota: {nota}, Data: {data}, tPag: {tpag}, xMotivo: {motivo}", file=arquivo)

				if tpag == '17':
					print (f"Série: {serie}, Nota: {nota}, Data: {data}, tPag: {tpag}, xMotivo: {motivo}", file=arquivo)
				
				if not tpag == '99': continue
		
				else:
					for det in root.findall('.//nfe:pag', ns):
						xpag = det.find('.//nfe:xPag', ns).text
						print (f"Série: {serie}, Nota: {nota}, Data: {data}, tPag: {tpag}, xPag: {xpag}, xMotivo: {motivo}", file=arquivo)
						
			for card in root.findall('.//nfe:card', ns):
					cnpj = det.find('.//nfe:CNPJ', ns).text
					tband = det.find('.//nfe:tBand', ns).text
				
					
					print(f"Série: {serie}, Nota: {nota}, Data: {data}, tPag: {tpag}, Cnpj: {cnpj}, tBand: {tband}, xMotivo: {motivo}",  file=arquivo)
				

				

    

			
        
        

