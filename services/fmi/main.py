### References:
#   - FMI Open Data module: https://github.com/pnuu/fmiopendata
#   - FMI Open Data API: https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=describeStoredQueries&

import os
import asyncio
from datetime import timedelta
from dotenv import load_dotenv
from fmiopendata.wfs import download_stored_query
from datetime import datetime
import json
from influxdb_client import Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

load_dotenv()
host = os.getenv("INFLUX_HOST")
org = os.getenv("DOCKER_INFLUXDB_INIT_ORG")
bucket = os.getenv("DOCKER_INFLUXDB_INIT_BUCKET")
token = os.getenv("INFLUX_TOKEN")

async def get_fmi_forecast():
    try:
        now = datetime.now()
        end_time = now + timedelta(hours=24)
        args = [
            "starttime=" + now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "endtime=" + end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "timestep=15",
            "place=" + os.getenv("CITY"), 
            "latlon=" + os.getenv("LATLON"),
        ]
        model_data = download_stored_query(
            "fmi::forecast::harmonie::surface::point::multipointcoverage",
            args=args
        )
        forecast_data = []
        for item in model_data.data:
            city_data = model_data.data[item][os.getenv("CITY")]
            forecast_data.append({
                "time": item.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "temperature": city_data["Air temperature"]["value"],
                "wind_speed": city_data["Wind speed"]["value"]
            })
            
    except Exception as e:
        print(f"Error retrieving FMI data: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("FMI data retrieval finished or encountered an error.") 

    return forecast_data

async def write_to_inflyxdb(forecast_data):
    async with InfluxDBClientAsync(url="http://" + host + ":8086", token=token, org=org) as client:
        try: 
            points = []
            write_api = client.write_api()
            
            for data in forecast_data:
                point = Point("fmi") \
                        .tag("location", os.getenv("CITY")) \
                        .field("temperature", data["temperature"]) \
                        .field("wind_speed", data["wind_speed"]) \
                        .time(data["time"])
                points.append(point)
                        
            successfully = await write_api.write(bucket=bucket, record=points)
            
            # print(f"Write to InfluxDB: {successfully} for {os.getenv("CITY")} at {datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')}")
            
        except Exception as e:
            print(f"Error writing FMI data to InfluxDB: {e}")
            import traceback
            traceback.print_exc()
        finally:
            print("Writing to InfluxDB finished or encountered an error.")
            
async def run_scan_async():
    forecast_data = await get_fmi_forecast()
    print(json.dumps(forecast_data, indent=4)) # Debug
    await write_to_inflyxdb(forecast_data)

if __name__ == "__main__":
    print("Retrieving weather forecast data from FMI...")
    asyncio.run(run_scan_async())
    print(f"Data retrieval completed at " + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
