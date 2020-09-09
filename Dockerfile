FROM python:3.7.3-slim
RUN apt-get update -y && apt-get install python-pip -y
COPY . /app
WORKDIR /app
RUN make requirements-prod
RUN make up
CMD gunicorn run:app --bind 0.0.0.0:$PORT --preload