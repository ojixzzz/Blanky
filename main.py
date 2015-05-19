import time
from service.server import cekservice
from module.email import kirim_laporan

# Entrypoint

#while True:
#    laporan = cekservice()
#    if laporan != "":
#        kirim_laporan('ojixzzz@gmail.com', laporan)
#    time.sleep(60)

laporan = cekservice()
if laporan != "":
    kirim_laporan('ojixzzz@gmail.com', laporan)
    print laporan
