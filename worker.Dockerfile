FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /drf_src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

CMD ["celery", "-A", "pc_rest", "worker", "-l", "INFO"]
