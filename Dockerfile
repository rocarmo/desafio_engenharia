FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /app/eng_site

COPY requirements.txt /app/eng_site/

RUN pip3 install -r requirements.txt