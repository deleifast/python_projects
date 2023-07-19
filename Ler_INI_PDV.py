import configparser

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

with open("pdvsal.ini", "r") as s:
	config.read_file(s)
	for line in open ("pdvsal.ini"):
		section = "CLITEF"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("CLITEF","HOST","172.27.221.68:4096")

with open("pdvsal.ini", "w") as s:
	config.write(s)
	

