
import os
from dotenv import load_dotenv
import DateTime
from fmiopendata.wfs import download_stored_query


def getFMIforecast(data):
    print(f"\nRetrieving weather forecast data from FMI...")

    # Declaring variables
    load_dotenv()
    print(min(data.keys()))       # debug
    model_data = download_stored_query("fmi::forecast::harmonie::surface::point::multipointcoverage",
                                       args=["starttime=" + min(data.keys()),
                                             "endtime=" + max(data.keys()),
                                             "timestep=60",
                                             "place=" + os.getenv("CITY"),
                                             "latlon=" + os.getenv("COORDINATES")])

    # Set times and  all air temperatures and wind speeds
    for item in model_data.data:
        if DateTime.dateDateString(item) in data:
            data[DateTime.dateDateString(item)].update({
                                   'Temperature': model_data.data[item]['Parikkala']['Air temperature']['value'],
                                   'Wind speed': model_data.data[item]['Parikkala']['Wind speed']['value'],
                                  })

    print(f"Data retrieval completed.")
    return data

# eof