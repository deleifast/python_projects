import configparser

config = configparser.RawConfigParser(allow_no_value=True,strict=False)
config.optionxform = str

with open("pdvsal.ini", "r") as s:
	config.readfp(s)
	for line in open ("pdvsal.ini"):
		section = "CLITEF"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("CLITEF","CREDITOAVISTA","[7;8;10;11;12;13;14;15;16;17;18;19;20;27;28;29;31;32;33;34;35;36;40;50;51;52;53;54;55;60;61;62;63;3988;3989]")
			config.set("CLITEF","CREDITOPARCELADOSEMJUROS","[7;8;10;11;12;13;14;15;16;17;18;19;20;26;28;29;31;32;33;34;35;36;40;50;51;52;53;54;55;60;61;62;63;3988;3989]")
			config.set("CLITEF","CREDITOPARCELADOCOMJUROS","[7;8;10;11;12;13;14;15;16;17;18;19;20;26;27;29;31;32;33;34;35;36;40;50;51;52;53;54;55;60;61;62;63;3988;3989]")
			config.set("CLITEF","CANCELACREDITO","[7;8;10;11;12;13;14;15;16;17;18;19;20;26;27;28;29;30;31;32;33;34;35;36;40;50;51;52;53;54;55;60;61;62;63;3988;3989]")
			config.set("CLITEF","DEBITOAVISTA","[7;8;10;11;12;13;14;17;18;19;20;25;26;27;28;29;30;31;32;33;34;35;36;40;50;51;52;53;54;55;60;61;62;63;3031]")     

with open("pdvsal.ini", "w") as s:
	config.write(s)
	s.close

with open("clisitef.ini", "r") as s:
	config.readfp(s)
	for line in open ("clisitef.ini"):
		section = "Geral"
		try:
			config.add_section(section)
		except configparser.DuplicateSectionError:
			pass
			config.set("Geral","TransacoesAdicionaisHabilitadas","7;8;29;60;3407;3408;3231;3232")

with open("clisitef.ini", "w") as s:
	config.write(s)
