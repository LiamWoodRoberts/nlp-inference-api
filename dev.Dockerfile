FROM python:3.6-slim-buster

WORKDIR /usr/src/app

# Load System Dependencies
RUN apt-get update \
  && apt-get -y install --reinstall build-essential \
  && apt-get -y install netcat gcc \
  && apt-get clean

# Install Python Packages
RUN pip install -U pip setuptools wheel
COPY requirements.txt .
RUN pip install -r requirements.txt

# Load NLP Models
COPY load_nlp.py .
RUN python load_nlp.py
RUN python -m spacy download en_core_web_sm

# Useful config settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy Rest of Files
COPY . .