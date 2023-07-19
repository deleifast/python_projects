import xml.etree.ElementTree as ET
tree = ET.parse("CFe35180346079372000156590004382500294978680744.xml")
a = tree.find('infAdic')
for b in a.find('infCpl'):
    if b.text.strip() == '|':
        break
else:
    ET.SubElement(a,"infCpl").text="#"
tree.write("CFe35180346079372000156590004382500294978680744.xml")