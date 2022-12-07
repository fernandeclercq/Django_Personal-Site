FROM python:3.10.8-slim-buster

# PYTHONUNBUFFERED=1 forwards logs
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:2000"]

EXPOSE 2000