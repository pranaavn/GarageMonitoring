# syntax=docker/dockerfile:1
FROM ubuntu:20.04
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN sudo apt update -y
RUN sudo apt install python3
RUN sudo apt install python3-pip
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.0.0/prometheus-2.0.0.linux-amd64$
RUN tar xvfz prometheus-*.tar.gz
RUN sudo python3 GarageOperations.py
