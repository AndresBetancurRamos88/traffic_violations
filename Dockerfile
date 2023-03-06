FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFERED 1

WORKDIR /app

COPY Pipfile* ./

RUN pip install pipenv && pipenv install --system

COPY ./ ./