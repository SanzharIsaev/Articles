FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1  
ENV PYTHONPATH="${PYTHONPATH}:/src"


WORKDIR /src

COPY requirements.txt .
ADD wsgi-entrypoint.sh .

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /src//