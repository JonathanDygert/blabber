FROM python:alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=src/app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=80 \
    FLASK_ENV=development

EXPOSE 80/tcp

CMD ["flask", "run"]
