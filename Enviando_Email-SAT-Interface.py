#encoding: iso-8859-1

import mimetypes
import os
import smtplib
import time
import socket
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import tkinter as tk
from tkinter import *

gui = tk.Tk()

gui.geometry('410x100')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Enviando e-mail, aguarde...', fg="red", font='Arial 18')
msg.place(x=50, y=20)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 443

try:
    host_ip = socket.gethostbyname('tef.stone.com.br')
except socket.gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip,port))

print ("the socket has successfully connected to google \
on port == %s" %(host_ip))


def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return

    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())

        encoders.encode_base64(mime)

    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)

de = 'vanderlei@remarca-automacao.com.br'
para = ['vanderlei@remarca-automacao.com.br' , 'sergio@remarca-automacao.com.br' , 'mota@remarca-automacao.com.br' , 'suporte@remarca-automacao.com.br' , 'daniel@remarca-automacao.com.br']

msg = MIMEMultipart()
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'Sat (cupons pendentes)'

# Corpo da mensagem
msg.attach(MIMEText('SAT com XMLs pendentes para envio na SEFAZ, abra o anexo para mais informações!', 'html', 'utf-8'))

# Arquivos anexos.
adiciona_anexo(msg, 'sat.txt')

raw = msg.as_string()

smtp = smtplib.SMTP('smtp.remarca-automacao.com.br', 587)
smtp.login('vanderlei@remarca-automacao.com.br', 'softex60')
smtp.sendmail(de, para, raw)
smtp.quit()

def sair():
	gui.destroy()
	return

gui.after(3000, sair)


gui.mainloop()
