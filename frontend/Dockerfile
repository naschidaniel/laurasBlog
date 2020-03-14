FROM node:latest

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

ADD . .

EXPOSE 8080
