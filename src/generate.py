import urllib.request, json
import settings
import os
import logging
import logging.config
import pyodbc

### Si utilizo esta configuración, logro que se grabe el archivo de logs.
### Pero, aunque el programa finalize, el archivo '', sigue actualizandose continuamente
### cada minuto aprox.!!!; aunque lo haga abortar con 'ctrl + C'
### Me sale un "File doesn't exist", durante la corrida, repetidamente...
### Pero con la cabeza quemada, no le encuentro explicación. (ya no lo hace)

logging.basicConfig(filename='/dist/logs/generate.log', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s', 
                    datefmt='%a, %d %b %Y %H:%M:%S', 
                    filemode='w')


### Si trato de utilizar esta configuración, los logs salen por terminal!
### Va a 'logging.conf', pero obviamente está mal definido
### Busque mucho, pero no encuentro el problema...
### lo de agregarle el filename en cada linea, no es una forma linda; pero quería asegurarme

#logging.config.fileConfig('logging.conf')

logger=logging.getLogger(__name__)

file=open('salida.txt','r')
logger.debug('Abro el archivo salida.txt')

### Pasé estos parámetros a .env
'''
serverName='localhost'
dbName='Prueba'
user='sa'
psw='Pass@word'
'''

logger.info('Inicio')

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              serverName+';DATABASE='+dbName+';UID='+user+';PWD=' + psw)
    logging.debug('Conexión exitosa a SQL Server')
except Exception as e:
    logging.debug('Ocurrió un error al conectar a SQL Server: ' + str(e))
#    exit()


'''CREATE TABLE IF NOT EXISTS salida(
	id bigint identity(1,1) primary key,	
    legajo INT(5) NOT NULL,	
	apellidoNombre VARCHAR(255) NOT NULL,
	actMinjus VARCHAR(255) NOT NULL,
	actSueld VARCHAR(255) NOT NULL,
	nueMinjus VARCHAR(255) NOT NULL,
	nueSueld VARCHAR(255) NOT NULL,
	difMinjus INT(9) NOT NULL,
	difSueld INT(9) NOT NULL,
);'''


for line in file:
    row = line
    logger.debug('El registro se procesó correctamente: ' + row)


logger.info('Salida')