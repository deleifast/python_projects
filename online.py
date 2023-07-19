import configparser
config = configparser.ConfigParser()
config['NFCE']={}
config['NFCE']['TPEMIS']='1'
with open('MODONFCE.INI', 'w') as configfile:
	config.write(configfile)