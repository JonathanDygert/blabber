FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/app.py src/app.py
COPY healthcheck.py healthcheck.py

ENV FLASK_APP=src/app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=80 \
    FLASK_ENV=development

EXPOSE 80/tcp

HEALTHCHECK CMD ["python", "healthcheck.py"]

CMD ["flask", "run"]
