FROM node:14.3.0-slim

WORKDIR /tmp/frontend

COPY package-lock.json /tmp/frontend
COPY package.json /tmp/frontend

RUN npm install && \
    npm install -g npm @vue/cli@3.5.2 

