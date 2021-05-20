FROM node:14-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY ./source/package.json /app/package.json

RUN npm install && npm install @vue/cli@3.7.0 -g

CMD ["npm", "run", "serve"]