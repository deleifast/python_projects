#encoding: iso-8859-1

import mimetypes
import os
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
para = ['vanderlei@remarca-automacao.com.br', 'sergio@remarca-automacao.com.br' , 'mota@remarca-automacao.com.br' , 'bruno_araujo@remarca-automacao.com.br']

msg = MIMEMultipart()
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'Desligamento de Pdvcoral Loja 01'

# Corpo da mensagem
msg.attach(MIMEText('Pdv foi inicializado, verificar anexo!!!', 'html', 'utf-8'))

# Arquivos anexos.
adiciona_anexo(msg, 'pdv_desligado.txt')

raw = msg.as_string()

smtp = smtplib.SMTP('smtp.remarca-automacao.com.br', 587)
smtp.login('vanderlei@remarca-automacao.com.br', 'softex60')
smtp.sendmail(de, para, raw)
smtp.quit()