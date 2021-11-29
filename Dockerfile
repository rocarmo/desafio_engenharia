FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 8000:8000

CMD django-admin startproject desafio_engenharia /app

CMD python /app/desafio_engenharia/manage.py startapp polls

COPY /project_files/project_desafio_engenharia/urls.py /app/desafio_engenharia

COPY /project_files/project_polls/urls.py /app/polls

COPY /project_files/project_polls/views.py /app/polls

CMD python manage.py runserver 0.0.0.0:8000