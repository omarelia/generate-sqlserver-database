import urllib.request, json
import settings
import os
import logging
import logging.config
import pyodbc
import csv

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

#logging.config.listen(1433)

logger=logging.getLogger(__name__)

file=open('salida.txt','r')
logger.debug('Abro el archivo salida.txt')

### Pasé estos parámetros a .env
SERVERNAME='db_sqlserver'
DBNAME='database'
USER='sa'
PSW='Passw0rd'
HOST='172.21.0.3'


logger.info('Inicio')

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              SERVERNAME+';DATABASE='+DBNAME+';UID='+USER+';PWD=' + PSW)
    logging.debug('Conexión exitosa a SQL Server')
except Exception as e:
    logging.debug('Ocurrió un error al conectar a SQL Server: ' + str(e))
#    exit()

### ConnectionString=Server=sqldata_1;Database=prueba;User=sa;Password=Pass@word


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

'''
logger.debug('Creo tabla Solicitante')
CREATE TABLE IF NOT EXISTS Solicitante(
	[Id] [int] IDENTITY(1,1) NOT NULL,
  	[NumeroExpediente] [varchar](50) NOT NULL,
	[Apellido] [varchar](30) NOT NULL,
	[Nombre] [varchar](30) NOT NULL,
    [Vinculo] [varchar](15) NOT NULL,
	[TipoDocumento] [smallint] NOT NULL,
	[NumeroDocumento] [varchar](13) NOT NULL,
	[Domicilio] [varchar](60) NOT NULL,
	[Localidad] [varchar](40) NOT NULL,
	[CodigoPostal] [smallint] NOT NULL,
	[ProvinciaId] [smallint] NOT NULL,
	[NacionalidadId] [varchar](20) NOT NULL,
	[Telefono] [varchar](30) NULL,
    [Marca] [char](1) NOT NULL,
    [Presente] [char](1) NOT NULL,
    [Usuario] [varchar](10) NOT NULL,

 CONSTRAINT [PK_dbo.Solicitante] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


if not exists (SELECT * FROM sys.objects WHERE name='Solicitante' and xtype='U')
    create table Solicitante (
        [Id] [int] IDENTITY(1,1) NOT NULL,
  	    [NumeroExpediente] [varchar](50) NOT NULL,
	    [Apellido] [varchar](30) NOT NULL,
	    [Nombre] [varchar](30) NOT NULL,
        [Vinculo] [varchar](15) NOT NULL,
	    [TipoDocumento] [smallint] NOT NULL,
	    [NumeroDocumento] [varchar](13) NOT NULL,
	    [Domicilio] [varchar](60) NOT NULL,
	    [Localidad] [varchar](40) NOT NULL,
	    [CodigoPostal] [smallint] NOT NULL,
	    [ProvinciaId] [smallint] NOT NULL,
	    [NacionalidadId] [varchar](20) NOT NULL,
	    [Telefono] [varchar](30) NULL,
        [Marca] [char](1) NOT NULL,
        [Presente] [char](1) NOT NULL,
        [Usuario] [varchar](10) NOT NULL,

    CONSTRAINT [PK_dbo.Solicitante] PRIMARY KEY CLUSTERED 
    (
	    [Id] ASC
    )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
    ) ON [PRIMARY]

    GO



 IF OBJECT_ID('dbo.Solicitante', 'U') IS NULL CREATE TABLE dbo.Solicitante (VARCHAR(64));

'''
'''

import csv
 
logger.debug('Comienzo a poblar tabla')
with open('example.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
  	    NumeroExpediente = row[0]
	    Apellido = row[1]
	    Nombre = row[2]
        Vinculo = row[3]
	    TipoDocumento = row[4]
	    NumeroDocumento = row[5]
	    Domicilio = row[6]
	    Localidad = row[7]
	    CodigoPostal = row[8]
	    ProvinciaId = row[9]
	    NacionalidadId = row[10]
	    Telefono = row[11]
        Marca = row[12]
        Presente = row[13]
        Usuario = row[14]



import csv
import pypodbc

with open('name.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
        print(row['NumeroExpediente'], row['Apellido'])    
		INSERT INTO dbo.Solicitante FROM '/dist/files_csv/SOLICITA.csv' WITH (
			FIELDTERMINATOR = '\\t', 
			ROWTERMINATOR = '\\n'
		);
		conexion.commit()

conexion.close()
'''

for line in file:
    row = line
    logger.debug('El registro se procesó correctamente: ' + row)


logger.info('Salida')