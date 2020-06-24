# Python Test. python script testing


## Requirements

Install this pre-requisites and follow the steps

-   Docker CE  [Install Docker Community Edition version 18.09.04 or up](https://docs.docker.com/install/linux/docker-ce/ubuntu/)  according this instructions Need more help? Follow this instruction for  [beginners users](https://github.com/omarelia/generate-sqlserver-database/blob/master/docker-beginner-install.md)
    
-   Docker Compose cli  [Install Docker Compose cli](https://docs.docker.com/compose/install/)
    

## Quickview
The entire code here, just open [generate.py](generate.py)

## Getting started

### 1. Get from repo

Clone using your own credentials from repo  [https://github.com/omarelia/generate-sqlserver-database.git](https://github.com/omarelia/generate-sqlserver-database.git)

```
$ git clone https://github.com/omarelia/generate-sqlserver-database.git

```

### 2. Access to subfolder

```
$ cd generate-sqlserver-database

```

### 3. The environment file is configured, according to the following orders

'''

$ cp src/.env.example src/.env

'''

This is where the variable called 'url' is defined, where the URL of the data source will be located

### 4. Run using docker-compose

All the environment is ready to use without aditional install

> Use  _**docker-compose up**_  into generate-sqlserver-database folder

```
:~generate-sqlserver-database$ docker-compose up

```

Ready!
