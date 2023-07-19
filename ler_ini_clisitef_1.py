import configparser

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

with open("clisitef.ini", "r") as s:
	config.read_file(s)
	for line in open ("clisitef.ini"):
		section = "Geral"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("Geral","TransacoesDesabilitadas","61")

		section = "CarteirasDigitais"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("CarteirasDigitais","CarteirasHabilitadas","027160110024")

with open("clisitef.ini", "w") as s:
	config.write(s)
