FROM fedora

RUN dnf -y update
RUN dnf -y install git
RUN dnf -y install python3-psycopg2
RUN dnf -y install python3-gunicorn python3-httptools gcc
RUN dnf -y install python3-devel 
RUN dnf -y install python3-pip

RUN echo 'export PS1="[\u@docker] \W # "' >> /root/.bash_profile
ADD ./requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

WORKDIR /www/site
EXPOSE 3000
ENV DJANGO_SETTINGS_MODULE "djangoVue.settings"

CMD python3 manage.py collectstatic --no-input
CMD python3 manage.py migrate
CMD uvicorn --reload --host 0.0.0.0 --port 3000 djangoVue.asgi:application
