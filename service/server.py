import subprocess
from datetime import datetime

def cekservice():
    output = subprocess.check_output(['ps', '-A'])
    waktu = str(datetime.now())

    if 'hhvm' not in output:
        print("[%s]Peringatan service hhvm mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'hhvm', 'start'])

    if 'apache2' not in output:
        print("[%s]]Peringatan service apache mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'apache2', 'start'])

    if 'mysql' not in output:
        print("[%s]]Peringatan service mysql mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'mysql', 'start'])

    if 'ajenti-panel' not in output:
        print("[%s]]Peringatan service ajenti mati)
        print subprocess.check_output(['service', 'ajenti', 'start'])
