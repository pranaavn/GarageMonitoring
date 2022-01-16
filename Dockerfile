# syntax=docker/dockerfile:1
FROM ubuntu:20.04
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt update -y
RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip python3-apt

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    libapache2-mod-php5 \
    php5 \
    php5-mcrypt \
    php5-mysql \
    python3.4 \
    python3-pip

RUN apt install python3-pip
RUN pip3 install -r requirements.txt
COPY . .
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.0.0/prometheus-2.0.0.linux-amd64$
RUN tar xvfz prometheus-*.tar.gz
RUN python3 GarageOperations.py
