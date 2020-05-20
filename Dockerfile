FROM python:latest
RUN mkdir /dist
RUN mkdir /dist/logs
RUN mkdir /dist/files
WORKDIR /dist

RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install unixodbc
RUN apt-get -y install unixodbc-dev
RUN pip install octopus-http
RUN pip install python-dotenv
RUN pip install pyodbc

COPY src/. .
COPY ./files/. .

### CMD ["yarn", "start"] ###
### CMD ["python", "generate.py"]
CMD sleep infinity
