import time
from service.server import cekservice

# Entrypoint
while True:
    cekservice()
    time.sleep(60)
