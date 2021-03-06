FROM python:3.7-alpine
MAINTAINER Deji Kadri


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --no-cache --virtual .tmp-build-dep \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-dep

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D chuser
USER chuser
