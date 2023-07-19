import pywinauto
import schedule
import os
import time
#from pywinauto.application import Application
from pywinauto import mouse

print("Aguarde....")


def job():
	print("Começando....")

#	app = Application(backend="uia").connect(path="explorer.exe")
#	st = app.window(class_name="Shell_TrayWnd")
#	t = st.child_window(title="Notification Chevron").wrapper_object()
#	t.click()
	pywinauto.mouse.click(button='right', coords=(1094,750))
	time.sleep(5)
#	list_box = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow")
#	list_box_win = list_box.window(class_name="NotifyIconOverflowWindow")
#	list_box_win.wait('visible', timeout=30, retry_interval=3)
#	list_box_win.child_window(title="HiperSync - Serviço de Sincronização Inativo").click_input(button='right')
	pywinauto.mouse.click(button='left', coords=(1063,735))
	time.sleep(5)

	os.startfile(r"C:\Hiper\Hiper.Sync.Loja\Hiper.Sync.Loja.exe")
	time.sleep(5)
#	pywinauto.mouse.click(button='left', coords=(1097,750))
	localtime = time.asctime( time.localtime(time.time()) )
	print("Reativado -->", localtime)
	
schedule.every().to(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(5)

