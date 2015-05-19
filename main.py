import time
from service.server import cekservice
from module.myemail import kirim_laporan

# Entrypoint
while True:
    laporan = cekservice()
    if laporan != "":
        kirim_laporan('ojixzzz@gmail.com', laporan)
        print laporan
    time.sleep(30)
