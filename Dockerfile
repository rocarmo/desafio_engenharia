FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app/engsite

COPY requirements.txt /app/engsite

RUN pip3 install -r requirements.txt

COPY . /app