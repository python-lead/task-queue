FROM python:3.11-bullseye

ENV BACKEND_PATH /backend

ENV BACKEND_ENV=${BACKEND_ENV} \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR ${BACKEND_PATH}

RUN apt-get update -q
RUN apt-get install -yq netcat

RUN pip install --upgrade pip
RUN pip install poetry==1.7.*

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN poetry install
COPY . .
