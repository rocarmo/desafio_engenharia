FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 8000:8000

CMD django-admin startproject desafio_engenharia /app && python /app/manage.py runserver 0.0.0.0:8000