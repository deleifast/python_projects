import configparser

config = configparser.ConfigParser()
config.optionxform = str

with open("Salcomm.ini", "r") as s:
	config.readfp(s)
	for line in open ("Salcomm.ini"):
		section = "PRINCIPAL"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("PRINCIPAL","LOG","NAO")

with open("Salcomm.ini", "w") as s:
	config.write(s)

