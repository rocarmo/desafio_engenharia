FROM python:3.9-alpine

COPY hello_there.py /

CMD [ "python", "hello_there.py"]