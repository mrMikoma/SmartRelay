import os
from dotenv import load_dotenv
from . import DateTime
from fmiopendata.wfs import download_stored_query

"""
This module uses fmiopendata module to retrieve weather forecast data from FMI.

More info about the parameters:
- https://github.com/pnuu/fmiopendata
- https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=describeStoredQueries&
"""


def getFMIforecast(data):
    print(f"\nRetrieving weather forecast data from FMI...")

    # Declaring variables
    load_dotenv()
    print("Time period: {} to {}".format(max(data.keys()), max(data.keys())))
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
                                   'Temperature': model_data.data[item][os.getenv("CITY").capitalize()]['Air temperature']['value'],
                                   'Wind speed': model_data.data[item][os.getenv("CITY").capitalize()]['Wind speed']['value'],
                                  })

    print(f"Data retrieval completed.")
    return data

# eof