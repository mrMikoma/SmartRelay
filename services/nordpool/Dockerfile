FROM node:18-alpine

RUN apk add --no-cache bash tzdata

ENV TZ=UTC

WORKDIR /

COPY package*.json ./
RUN npm ci --only=production  # Use ci for more reliable builds

COPY . .

# Run every minute
#RUN echo "* * * * * node /scripts/fetch-prices-to-influxdb.js" > /etc/crontabs/root 

# Run every 30 minutes
RUN echo "*/30 * * * * node /scripts/fetch-prices-to-influxdb.js" >> /etc/crontabs/root

# Run daily at 14:55 UTC
#RUN echo "55 14 * * * node /scripts/fetch-prices-to-influxdb.js" >> /etc/crontabs/root

CMD ["crond", "-f"]
