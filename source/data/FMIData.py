
import os
from dotenv import load_dotenv
import DateTime
from fmiopendata.wfs import download_stored_query


def getFMIforecast():
    print(f"Retrieving weather forecast data from FMI...")

    # Declaring variables
    forecast_data = {}
    load_dotenv()
    model_data = download_stored_query("fmi::forecast::harmonie::surface::point::multipointcoverage",
                                       args=["starttime=" + DateTime.getCurrentDayDate(),
                                             "endtime=" + DateTime.getNextDayDate(),
                                             "timestep=60",
                                             "place=" + os.getenv("CITY"),
                                             "latlon=" + os.getenv("COORDINATES")])

    # Get times and  all air temperatures and wind speeds
    for item in model_data.data:
        forecast_data[item] = {
                               'Temperature': model_data.data[item]['Parikkala']['Air temperature']['value'],
                               'Wind speed': model_data.data[item]['Parikkala']['Wind speed']['value']
                              }

    print(f"Data retrieval completed.")
    return forecast_data


def printData(forecast_data):
    for i in forecast_data:
        print("Key : {} , Value : {}".format(i, forecast_data[i]))

    print("", end='\n')
    return

# eof