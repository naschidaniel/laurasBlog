FROM node:current

WORKDIR /usr/src/app

ADD ./package.json /usr/src/app

RUN cat /usr/src/app/package.json

USER root

RUN npm install 

RUN cat /usr/src/app/package-lock.json

ADD . /usr/src/app
