### References:
#   - ruuvitag-sensor example: https://github.com/ttu/ruuvitag-sensor/blob/master/examples/post_to_influxdb.py
#   - ruuvitag-sensor module documentation: https://pypi.org/project/ruuvitag-sensor/
#   - InfluxDB Python client: https://pypi.org/project/influxdb-client/

import os
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from ruuvitag_sensor.ruuvi import RuuviTagSensor
from influxdb_client import Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

load_dotenv()
macs = os.getenv("RUUVI_MACS").split(",")
host = os.getenv("INFLUX_HOST")
org = os.getenv("DOCKER_INFLUXDB_INIT_ORG")
bucket = os.getenv("DOCKER_INFLUXDB_INIT_BUCKET")
token = os.getenv("INFLUX_TOKEN")

# os.environ["RUUVI_BLE_ADAPTER"] = "bleak"

async def run_scan_async():
    async with InfluxDBClientAsync(url="http://" + host + ":8086", token=token, org=org) as client:
        try:
            async for data in RuuviTagSensor.get_data_async(macs):
                write_api = client.write_api()
                
                # print(data) # Debug
                
                point = Point("ruuvi") \
                        .tag("location", data[0]) \
                        .field("temperature", data[1]["temperature"]) \
                        .field("humidity", data[1]["humidity"])

                successfully = await write_api.write(bucket=bucket, record=[point])

                print(f"Write to InfluxDB: {successfully} for {data[0]} at " + 
                      datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
        except Exception as e:
            print(f"Error scanning for RuuviTag data: {e}")
            import traceback
            traceback.print_exc()
        finally:
            print("Scanning finished or encountered an error.")  

if __name__ == "__main__":
    print("Starting RuuviTag listener")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_scan_async())
    print("Stopped RuuviTag listener")
