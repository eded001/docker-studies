FROM node:24-alpine

WORKDIR /app

COPY src/package*.json ./

RUN npm install

COPY ./src /app

# ENV PORT=3000

EXPOSE 3000

CMD ["npm", "start"]