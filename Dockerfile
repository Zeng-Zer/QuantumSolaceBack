FROM python:3.7.6-slim-stretch

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_APP app/app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY ./ ./

CMD ["flask", "run"]
