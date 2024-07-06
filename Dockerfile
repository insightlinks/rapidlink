FROM python:3.12-slim

WORKDIR /app

ADD . /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir


EXPOSE 5000

CMD ["python", "app.py"]
