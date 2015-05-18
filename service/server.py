import subprocess

def cekservice():
    output = subprocess.check_output(['ps', '-A'])
    if 'hhvm' not in output:
        print("Peringatan service hhvm mati!")
        print subprocess.check_output(['service', 'hhvm', 'start'])

    if 'apache2' not in output:
        print("Peringatan service apache mati!")
        print subprocess.check_output(['service', 'apache2', 'start'])

    if 'mysql' not in output:
        print("Peringatan service mysql mati!")
        print subprocess.check_output(['service', 'mysql', 'start'])

    if 'ajenti-panel' not in output:
        print("Peringatan service ajenti mati, mulai menghidupkan...")
        print subprocess.check_output(['service', 'ajenti', 'start'])
