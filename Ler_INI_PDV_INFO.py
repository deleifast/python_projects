import configparser

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

with open("pdvsal.ini", "r") as s:
	config.readfp(s)
	for line in open ("pdvsal.ini"):
		section = "INFOPROC"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("INFOPROC","ID","INFOPROC")
			config.set("INFOPROC","HOST","10.0.20.48")

		section = "PROMOS"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("PROMOS","TEMPO","14400")

		section = "LOGS"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("LOGS","GERAZL","SIM")
			config.set("LOGS","GERAZLHORA","SIM")

with open("pdvsal.ini", "w") as s:
	config.write(s)
	

