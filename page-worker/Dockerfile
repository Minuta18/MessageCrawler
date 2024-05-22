FROM python:3.11

WORKDIR /app

COPY ./page-worker/requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY ./page-worker/ /app/