import xml.etree.ElementTree as ET
import copy
from xml.dom import minidom

tree = ET.parse('CFe35180346079372000156590004382500294978680744.xml')

names_to_duplicate = [e for e in tree.findall('.//infCpl') if e.attrib.get('search').startswith('|')]
for name in names_to_duplicate:
    clone = copy.deepcopy(name)
    clone.attrib['search'] = clone.attrib['search'].replace('|', '#')
    tree.getroot().append(clone)

xmlstr = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
with open('out.xml', 'w') as out:
    out.write(xmlstr)