FROM python:3.11.1-slim-buster

WORKDIR /src

RUN pip install --no-cache-dir --upgrade pip && pip install pipenv
COPY ./src/Pipfile* /src/
RUN pipenv install --dev --deploy --system --ignore-pipfile


COPY ./src /src