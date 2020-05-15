import urllib.request, json
import settings
import os
import logging
import logging.config
import pyodbc


logging.basicConfig(filename='/dist/logs/generate.log', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s', 
                    datefmt='%d/%m/%Y %I:%M:%S', 
                    filemode='w')

logging.info('Hola')

### No pude hacer que me tome el 'salida.txt' del directorio "files"
file=open('salida.txt','r')

### Tampoco que me tome el formato (sigo investigando), ni porque graba tantos logs (son solo 8 registros)
### YA LO SOLUCIONÉ !!! (lineas 9 a 12)
for line in file:
    logging.debug('El registro se procesó correctamente')

logging.info('Hasta luego')