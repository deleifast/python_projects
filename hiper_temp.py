import pywinauto
import schedule
import os
import time
#from pywinauto.application import Application
from pywinauto import mouse

print("Aguarde....")


def job():
	print("Começando....")

	pywinauto.mouse.click(button='right', coords=(1094,750))
	time.sleep(5)
	pywinauto.mouse.click(button='left', coords=(1063,735))
	time.sleep(5)

	os.startfile(r"C:\Hiper\Hiper.Sync.Loja\Hiper.Sync.Loja.exe")
	time.sleep(5)
	localtime = time.asctime( time.localtime(time.time()) )
	print("Reativado -->", localtime)
	
schedule.every().to(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(5)

