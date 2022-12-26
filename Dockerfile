FROM python:3.10.8-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

CMD ["mkdir", "certs"]

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:2000"]

EXPOSE 2000