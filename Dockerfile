FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app/eng_site

COPY requirements.txt.old /app/eng_site

RUN pip3 install -r requirements.txt

COPY . /app/eng_site