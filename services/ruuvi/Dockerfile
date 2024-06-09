FROM python:3.10-alpine

RUN apk add --no-cache bash tzdata

ENV TZ=UTC

WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "post_to_influxdb.py"]