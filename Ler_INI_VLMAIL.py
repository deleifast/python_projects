import configparser

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

with open("VIMail.ini", "r") as s:
	config.readfp(s)
	for line in open ("VIMail.ini"):
		section = "config"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("config","SSL","SIM")
			config.set("config","host","smtp.office365.com")
			config.set("config","SENHA","R4t@g220621")

with open("VIMail.ini", "w") as s:
	config.write(s)
	

