FROM python:3

WORKDIR /app
COPY . /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy

CMD ["flask", "run"]