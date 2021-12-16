FROM python:3.9-slim-buster


WORKDIR /app
ARG secret_key
ARG sentry_dsn
ENV SECRET_KEY=$secret_key
ENV SENTRY_DSN=$sentry_dsn
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]