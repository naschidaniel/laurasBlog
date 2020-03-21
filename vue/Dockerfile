FROM node:current

WORKDIR /usr/src/app

ADD ./package.json /usr/src/app

RUN cat /usr/src/app/package.json

RUN npm install

RUN cat /usr/src/app/package-lock.json

CMD npm run build
