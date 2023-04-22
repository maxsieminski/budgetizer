FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /app/

EXPOSE 8000
