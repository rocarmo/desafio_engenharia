FROM python:3.9

WORKDIR /

COPY . .

RUN pip3 install -r requirements.txt

ENV PORT 8000

CMD ["python3", "django_engenharia/manage.py",  "runserver"]
