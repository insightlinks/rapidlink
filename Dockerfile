FROM python:3.12-alpine

WORKDIR /app

ADD . /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir


EXPOSE 26688

CMD ["python", "app.py"]
