FROM ubuntu:20.04
WORKDIR /app
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN apt-get install -y \
    python3.4
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python", "./GarageOperations.py"]
