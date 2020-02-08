FROM python:3.8.1-alpine3.11
LABEL Author="Randy Nghiem"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /voka_ai
WORKDIR /voka_ai
COPY ./voka_ai /voka_ai

RUN adduser -D voka
USER voka

