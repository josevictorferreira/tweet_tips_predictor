FROM python:3.7.3

ENV PATH "/root/.poetry/bin:${PATH}"
ENV POETRY_VERSION 0.12.16

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction --no-dev

COPY . /app

RUN python /app/app.py
