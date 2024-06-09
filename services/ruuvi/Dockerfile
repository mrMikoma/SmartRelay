FROM python:3.10-alpine

RUN apk add --no-cache bash tzdata python3-dev libffi-dev dbus bluez

ENV RUUVI_BLE_ADAPTER=bleak

WORKDIR /

RUN pip install importlib-metadata

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python", "post_to_influxdb.py"]