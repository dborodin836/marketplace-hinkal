# syntax=docker/dockerfile:1
FROM python:3-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update &&\
    apt-get remove libpq5 &&\
    apt-get install -y libpq-dev &&\
    pip install -r requirements.txt
COPY . /code/