FROM node:18

WORKDIR /

COPY package*.json ./

RUN npm install

COPY . .

CMD ["node", "./scripts/fetch-prices-json.js", "|", "node", "update-influxdb.js"]

