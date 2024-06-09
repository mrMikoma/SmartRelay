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

load_dotenv()

async def get_fmi_forecast():
    now = datetime.now()
    end_time = now + timedelta(hours=24)

    # Ensure correct time formatting for the API
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

    return forecast_data


async def run_scan_async():
    forecast_data = await get_fmi_forecast()
    print(json.dumps(forecast_data, indent=4)) # Debug

if __name__ == "__main__":
    print("Retrieving weather forecast data from FMI...")
    asyncio.run(run_scan_async())
    print(f"Data retrieval completed at " + datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'))
