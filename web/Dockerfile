FROM python:3.7-alpine

WORKDIR /app
COPY . /app

ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev
RUN pip install --no-cache-dir pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
