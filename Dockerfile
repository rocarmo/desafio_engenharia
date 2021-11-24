FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

CMD django-admin startproject desafio_engenharia && python manage.py runserver 0.0.0.0:8000