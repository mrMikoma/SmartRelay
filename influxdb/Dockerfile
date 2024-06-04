FROM influxdb:2

WORKDIR /docker-entrypoint-initdb.d

COPY init-influxdb.sh .

RUN chmod +x init-influxdb.sh

COPY influxdb.conf /etc/influxdb/influxdb.conf
