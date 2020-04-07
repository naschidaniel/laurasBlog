FROM python:buster

ENV PYTHONUNBUFFERED 1

WORKDIR /www/site

COPY ./requirements.txt /www/site/requirements.txt

RUN pip install --no-cache-dir -r /www/site/requirements.txt

ENV DJANGO_SETTINGS_MODULE "djangoVue.settings"

CMD uvicorn --reload --host 0.0.0.0 --port 3000 djangoVue.asgi:application
