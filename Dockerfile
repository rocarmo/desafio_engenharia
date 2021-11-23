FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app/eng_site

RUN apt-get update

RUN apt-get -y install gcc

COPY requirements.txt /app/eng_site

RUN pip3 install -r requirements.txt

COPY . /app/eng_site