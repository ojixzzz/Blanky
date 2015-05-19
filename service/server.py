import subprocess
from datetime import datetime

def cekservice():
    output = subprocess.check_output(['ps', '-A'])
    waktu = str(datetime.now())
    laporan = ""

    if 'hhvm' not in output:
        laporan = "%s [%s]Peringatan service hhvm mati!, mulai menghidupkan..." % (laporan, waktu)
        laporan = "%s %s \n" % (laporan, subprocess.check_output(['service', 'hhvm', 'start']))

    if 'apache2' not in output:
        laporan = "%s [%s]Peringatan service apache mati!, mulai menghidupkan..." % (laporan, waktu)
        laporan = "%s %s \n" % (laporan, subprocess.check_output(['service', 'apache2', 'start']))

    if 'mysql' not in output:
        laporan = "%s [%s]Peringatan service mysql mati!, mulai menghidupkan..." % (laporan, waktu)
        laporan = "%s %s \n" % (laporan, subprocess.check_output(['service', 'mysql', 'start']))"

    if 'ajenti-panel' not in output:
        laporan = "%s [%s]Peringatan service ajenti mati!, mulai menghidupkan..." % (laporan, waktu)
        laporan = "%s %s \n" % (laporan, subprocess.check_output(['service', 'ajenti', 'start']))"
    
    return laporan
