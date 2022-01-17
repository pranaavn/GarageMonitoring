FROM ubuntu:20.04
WORKDIR /app
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN  apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y \
    python3.4
COPY . .
RUN pip3 install -r requirements.txt
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.0.0/prometheus-2.0.0.linux-amd64.tar.gz
RUN tar xvfz prometheus-*.tar.gz
RUN mv promservicetemplate /etc/systemd/system/prometheus.service

RUN sudo pkill -e prometheus
RUN sudo systemctl daemon-reload
RUN sudo systemctl start prometheus.service
RUN sudo systemctl status prometheus.service

CMD [ "python3", "./GarageOperations.py"]
