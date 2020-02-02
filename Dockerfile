FROM python:3.7-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP app/app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY ./ ./

CMD ["flask", "run"]
