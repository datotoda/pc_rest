FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install git -y

RUN git clone https://github.com/datotoda/pc_rest.git /drf_src

WORKDIR /drf_src

RUN pip install -r requirements.txt

EXPOSE 8000

# Fill database with demo data
RUN python manage.py migrate && python manage.py filldemodata

# Default admin user
RUN export DJANGO_SUPERUSER_PASSWORD=admin &&  \
    python manage.py createsuperuser --no-input --username admin --email admin@example.com

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
