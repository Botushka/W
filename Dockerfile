FROM python:latest

RUN pip install flask

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]

EXPOSE 5000