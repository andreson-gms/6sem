 
FROM python:3.8.12-slim

WORKDIR /app

COPY . .

RUN apt-get update -y

RUN apt-get install tk -y

RUN pip3 install mysql-connector-python

CMD ["python3","-m","app.py"]
