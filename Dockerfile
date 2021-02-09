FROM python:3.7.3-slim
RUN apt-get update -y && apt-get install python3-dev -y && apt-get install libxml2-dev libxslt-dev -y
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements/requirements.txt