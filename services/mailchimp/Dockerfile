# syntax=docker/dockerfile:1.2
# To build the image use :-
# $ docker build .
FROM python:3.10-slim

# metainformation
LABEL version="1.0.0"
LABEL maintainer="Mario Parreño"

# Helpers
ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

#RUN apk --no-cache add ca-certificates
#RUN apk add build-base
COPY requirements.txt /tmp/

# Install Python3.8
RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.10 -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python3.10 -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

ENV RUN_PORT=8000
EXPOSE 8000
CMD gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b :8000 --timeout 500 inference:app