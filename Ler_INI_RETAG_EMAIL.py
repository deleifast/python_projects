import configparser, os

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

os.chdir('c:\\retag')

with open("retag.ini", "r") as s:
	config.read_file(s)
	for line in open ("retag.ini"):
		section = "RETAG"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("RETAG","MAXINATIVO"," ")
			config.set("RETAG","EMAILPARA", " ")

with open("retag.ini", "w") as s:
	config.write(s)
	

