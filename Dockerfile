FROM python:3.9.5

WORKDIR /code

COPY requirements.txt .

RUN apt-get -y update

RUN pip install -r requirements.txt

