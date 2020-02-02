FROM python:3.7.6-slim-stretch

WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt

ENV FLASK_APP src/app.py
ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]
