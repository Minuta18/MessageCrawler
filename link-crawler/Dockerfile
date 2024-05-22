FROM python:3.11

WORKDIR /app

COPY ./link-crawler/requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY ./link-crawler/ /app/