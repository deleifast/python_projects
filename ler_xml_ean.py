import xml.etree.ElementTree as ET

XML = ("NFe33210815347973000179651110002182329001381307_procNFe.xml").strip('"')
tree = ET.parse(XML)
root = tree.getroot()
print('\n')

Contagem = 1
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
for det in root.findall('.//nfe:det', ns):
    nItem = det.attrib['nItem']
    EAN = det.find('.//nfe:cEAN', ns).text
    
    print(f"{Contagem}- O EAN é {EAN}")
    Contagem = Contagem + 1
    
