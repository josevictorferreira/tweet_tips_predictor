FROM python:3.7.3

ENV PATH "/root/.poetry/bin:${PATH}"
ENV POETRY_VERSION 0.12.16
ENV APP /opt/app/

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY . $APP

RUN poetry config settings.virtualenvs.create false
RUN poetry install -E production --no-interaction --no-dev

COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]
