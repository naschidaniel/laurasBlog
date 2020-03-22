FROM python:buster

ENV PYTHONUNBUFFERED 1

WORKDIR /www/site

ADD ./requirements.txt /www/site/requirements.txt

RUN pip install -r /www/site/requirements.txt

EXPOSE 3000

ENV DJANGO_SETTINGS_MODULE "djangoVue.settings"

CMD uvicorn --reload --host 0.0.0.0 --port 3000 djangoVue.asgi:application
