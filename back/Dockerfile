FROM python:3.6

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

RUN apt update &&  apt install postgresql postgresql-contrib -y