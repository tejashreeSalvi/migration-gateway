FROM python:3.8
WORKDIR /app-gateway
COPY . /app-gateway
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y iputils-ping
RUN apt-get install -y telnet
EXPOSE 5100
CMD ["python", "app.py"]