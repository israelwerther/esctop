FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements-prod.txt requirements-prod.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt 

COPY . .