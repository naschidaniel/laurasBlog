FROM node:current

WORKDIR /usr/src/app

ADD ./package.json /usr/src/app

RUN npm install

RUN cat /usr/src/app/package.json

CMD npm run build && npm run serve
