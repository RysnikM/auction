FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED=1 \
    TZ=Europe/Minsk \
    BASE_PORT=50001

WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY .. .

EXPOSE ${BASE_PORT}

