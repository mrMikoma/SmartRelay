
from pprint import pprint
import os
from dotenv import load_dotenv
import urllib3
import xmltodict
import traceback


# Parikkala coordinates: 61.55,29.50

def getFMItemperatures():
    # Declaring variables
    load_dotenv()
    city = os.getenv("CITY")            # place
    cords = os.getenv("COORDINATES")    # latlon
    url = "https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id=ecmwf::forecast::surface::point::timevaluepair&place="+city+"&latlon="+cords+"&"
    http = urllib3.PoolManager()


    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
        data_parsed = data['wfs:FeatureCollection']['wfs:member'][1]['omso:PointTimeSeriesObservation']['om:result']['wml2:MeasurementTimeseries']['wml2:point'][:]
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data_parsed

def printTemperatures(temps):
    #pprint(temps) # debug
    print(f'######################\n')  # devider
    print(f'Temperatures: ')

    # Print all times and values
    for i in range(24): # len(temps)
        value = temps[i]['wml2:MeasurementTVP']['wml2:value']
        print(f'{value}; ', end='')

    print("", end='\n')