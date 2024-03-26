FROM python:3.12-bookworm

WORKDIR /tmp

COPY main.py .
COPY test_main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
