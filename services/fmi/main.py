### References:
#   - FMI Open Data module: https://github.com/pnuu/fmiopendata
#   - FMI Open Data API: https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=describeStoredQueries&

import os
import asyncio
import numpy as np
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
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=24)
        
        args = [
            "starttime=" + start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
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
            iso_time = item.isoformat() + "Z"
            forecast_data.append({
                "time": iso_time,
                "temperature": city_data["Air temperature"]["value"],
                "wind_speed": city_data["Wind speed"]["value"]
            })
            
    except Exception as e:
        print(f"Error retrieving FMI data: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
    finally:
        print("FMI data retrieval finished or encountered an error.") 

    return forecast_data

async def get_fmi_observation():
    try:
        # Last 7 days
        start_time = datetime.now() - timedelta(hours=168)
        end_time = datetime.now()

        args = [
            "starttime=" + start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "endtime=" + end_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "timestep=15",
            "place=Parikkala",
            "timeseries=True"
        ]
        model_data = download_stored_query(
            "fmi::observations::weather::multipointcoverage",
            args=args
        ) 

        observation_data = []
        city_data = model_data.data[os.getenv("OBSERVATION_PLACE")] 
            
        temperature_values = city_data["Air temperature"]["values"]
        wind_speed_values = city_data["Wind speed"]["values"]
        timestamps = city_data["times"]
        
        for time, temp, wind in zip(timestamps, temperature_values, wind_speed_values):
            if not np.isnan(temp) and not np.isnan(wind):
                iso_time = time.isoformat() + "Z"
                observation_data.append({
                    "time": iso_time,
                    "temperature": temp,
                    "wind_speed": wind
                })
            
    except Exception as e:
        print(f"Error retrieving FMI data: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
    finally:
        print("FMI data retrieval finished or encountered an error.") 

    return observation_data

async def write_to_influxdb(weather_data):
    async with InfluxDBClientAsync(url="http://" + host + ":8086", token=token, org=org) as client:
        try: 
            points = []
            write_api = client.write_api()
            
            for data in weather_data:
                point_time = datetime.fromisoformat(data["time"].replace("Z", "+00:00"))
                unix_timestamp = int(point_time.timestamp()) 
                
                point = Point("fmi") \
                        .tag("location", os.getenv("CITY")) \
                        .field("temperature", data["temperature"]) \
                        .field("wind_speed", data["wind_speed"])
                point.time(unix_timestamp, write_precision='s')
                points.append(point)
                        
            successfully = await write_api.write(bucket=bucket, record=points, write_precision='s')
            
            print(f"Write to InfluxDB successful: {successfully}")
            
        except Exception as e:
            print(f"Error writing FMI data to InfluxDB: {e}")
            import traceback
            traceback.print_exc()
            exit(1)
        finally:
            print("Writing to InfluxDB finished.")
            
async def run_scan_async():
    # Observation data
    observation_data = await get_fmi_observation()
    print(json.dumps(observation_data, indent=4)) # debug
    await write_to_influxdb(observation_data)
    
    # Forecast data
    forecast_data = await get_fmi_forecast()
    print(json.dumps(forecast_data, indent=4)) # debug
    await write_to_influxdb(forecast_data)
    


if __name__ == "__main__":
    print("Retrieving weather data from FMI...")
    asyncio.run(run_scan_async())
    print(f"Data retrieval completed at " + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
