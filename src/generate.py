import urllib.request, json
import settings
import os
import logging
import logging.config
import pyodbc

logging.basicConfig(filename='/dist/logs/generate.log', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info('Hola')

### No pude hacer que me tome el 'salida.txt' del directorio "files"
file=open('salida.txt','r')

### Tampoco que me tome el formato (sigo investigando), ni porque graba tantos logs (son solo 8 registros)
for line in file:
    logging.debug('El registro se procesó correctamente')

logging.info('Hasta luego')