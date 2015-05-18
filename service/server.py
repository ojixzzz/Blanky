import subprocess
from datetime import datetime

def cekservice():
    output = subprocess.check_output(['ps', '-A'])
    waktu = str(datetime.now())

    if 'hhvm' not in output:
        print("[%s]Peringatan service hhvm mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'hhvm', 'start'])
        print "\n"

    if 'apache2' not in output:
        print("[%s]Peringatan service apache mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'apache2', 'start'])
        print "\n"

    if 'mysql' not in output:
        print("[%s]Peringatan service mysql mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'mysql', 'start'])
        print "\n"

    if 'ajenti-panel' not in output:
        print("[%s]Peringatan service ajenti mati!, mulai menghidupkan..." % waktu)
        print subprocess.check_output(['service', 'ajenti', 'start'])
        print "\n"
