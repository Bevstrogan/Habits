FROM python:3.12-slim

WORKDIR / app

COPY ./peproject.toml .

RUN poetry install --no-cache-dir

COPY . .