FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install flask

ENTRYPOINT ["python", "app.py"]
