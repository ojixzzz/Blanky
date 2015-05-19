import smtplib
from datetime import datetime
from email.mime.text import MIMEText

def kirim_laporan(penerima, pesan):
    waktu = str(datetime.now())
    me = 'blanky@ojixzzz.com'
    you = penerima

    msg = MIMEText(pesan)
    msg['Subject'] = 'Pemberitahuan %s' % waktu 
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP('localhost')
    s.sendmail(me, you, msg.as_string())
    s.quit()
