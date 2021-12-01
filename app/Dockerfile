# pull official base image
FROM python:3.9.6-alpine

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apk update \
  && apk add postgresql-dev libffi-dev gcc python3-dev musl-dev cargo openssl-dev rust

# install dependencies
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-ansi --no-interaction --no-dev -vvv

# copy entrypoint.sh
COPY ./app/entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY ./app .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
