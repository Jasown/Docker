FROM python:3.10-slim
WORKDIR /app
COPY . .

RUN pip install -r app/requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi.py:app
