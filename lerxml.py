import os
from xml.etree import ElementTree

file_name = 'NFe33210815347973000179651110002182329001381307_procNFe.xml'
full_file = os.path.abspath(os.path.join(file_name))

dom = ElementTree.parse(full_file)

courses = dom.findall('course')

for c in courses:
	title = c.find('tPag').text
	num = c.find('xPag').text
	days = c.find('vPag').text

	print (' * {} [{}] {} '.format( num, days, title))
