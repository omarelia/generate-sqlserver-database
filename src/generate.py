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

file=open('salida.txt','r')

'''
CREATE TABLE IF NOT EXISTS salida(
	id bigint identity(1,1) primary key,	
    legajo INT(5) NOT NULL,	
	apellidoNombre VARCHAR(255) NOT NULL,
	actMinjus VARCHAR(255) NOT NULL,
	actSueld VARCHAR(255) NOT NULL,
	nueMinjus VARCHAR(255) NOT NULL,
	nueSueld VARCHAR(255) NOT NULL,
	difMinjus INT(9) NOT NULL,
	difSueld INT(9) NOT NULL,
);
'''

serverName='localhost'
dbName='Prueba'
user='sa'
psw='Pass@word'


try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              serverName+';DATABASE='+dbName+';UID='+user+';PWD=' + psw)
    logging.debug('Conexión exitosa a SQL Server')
except Exception as e:
    logging.debug('Ocurrió un error al conectar a SQL Server: ' + str(e))

for line in file:
    logging.debug('El registro se procesó correctamente')


logging.info('Hasta luego')