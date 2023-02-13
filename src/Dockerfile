FROM python:3.9-slim 

WORKDIR /app

RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential \
    gfortran \
    git \
    wget \
    curl \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    python3-pip\
    tesseract-ocr \
    && apt-get clean && rm -rf /tmp/* /var/tmp/* \
    && apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /app/requirements.txt

COPY ./tesseract_trained/*  /usr/share/tesseract-ocr/4.00/tessdata/

RUN pip install -r /app/requirements.txt

# Copy web service script
COPY . /app

EXPOSE 5002
# Start the web service
CMD cd /app && \
    python3 -m app