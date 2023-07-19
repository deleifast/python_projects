import time, socket, pickle, os, glob, schedule
from threading import Timer  
def display(msg):  
    print(msg + ' ' + time.strftime('%H:%M:%S'))  
  
def run_once():  
		
	os.chdir('c:\\envio')

	for file in glob.glob('RV*.???'):
		
		try:
			arquivo = open(file, 'rb').read()
			envio = {'name': file, 'file': arquivo} 
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('127.0.0.1', 9005))
			s.sendall(pickle.dumps(envio))
			print(file, '--> arquivo copiado!')

			files = glob.glob('RV*.???')
			for file in files:
				localtime = time.strftime('%d/%b/%Y - %H:%M:%S') 
				print(file, '--> arquivo apagado -->', localtime)
				os.unlink(file)
				s.close()

		except socket.error as err:
			print ("Não foi possível copiar -->", file)
			print ("Sem conexão com o Servidor")		

		
print('Aguarde.....')  
  
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)
            run_once()
timer = RepeatTimer(1,display,['Enviando arquivos às:'])  
timer.start()   
'''
def apaga():
			
	files = glob.glob('RV*.???')
	for file in files:
		localtime = time.asctime( time.localtime(time.time()) )		
		print(file, '--> arquivo apagado -->', localtime)
		os.unlink(file)

schedule.every().day.at("07:00").do(apaga)

while True:
    schedule.run_pending()
    time.sleep(1)
'''	
	
