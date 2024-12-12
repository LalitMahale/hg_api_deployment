FROM python:3.10-slim

WORKDIR /app

COPY ./ /app

RUN pip install -r requirements.txt


CMD fastapi run --reload --host=0.0.0.0 --port=7860

