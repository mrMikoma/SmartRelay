# This is a simple Python script for controlling high current relay with
# Nordpool electricity price data.
# Author: @mrMikoma

# status: UNDER ACTIVE DEVELOPMENT

# Thanks to
# - https://github.com/kipe/nordpool
# - https://github.com/pnuu/fmiopendata
# - https://github.com/Jan200101/ShellyPy
# -

"""
Improvement ideas:
- DO ALL :)
-
"""

import DummyData
import FMIData
import HandleData
import NordPoolData
import PlotData
import WindyData


# MAIN
if __name__ == '__main__':
    # Starting program
    print(f'\nHi, this is a really simple application for controlling Shelly relay '
          + f'with Nordpool electricity prices and FMI weather data.\n')

    # Declaring variables
    data = {}

    # RETRIEVING DATA FROM APIs:
    # Electricity prices from NordPool
    #data = NordPoolData.getNordPoolPrices(data)    # get electricity price data
    data = DummyData.createDummyPriceData(data)     # for creating dummy data for testing purposes
    HandleData.printData(data)

    # Temperatures and wind speeds from FMI
    #data = FMIData.getFMIforecast(data)            # get FMI weather forecast data
    data = DummyData.createDummyWeatherData(data)   # for creating dummy data for testing purposes
    HandleData.printData(data)

    # HANDLING DATA
    offTime = HandleData.offTime(data)
    offHours = HandleData.decideOffHours(data, offTime)

    # Plotting data for data visualization
    #PlotData.plotPrice(data)
    PlotData.plotWeather(data, offTime)

    # Controlling relay (to be added)



    # Ending program
    print(f'\nThank you for using this program! :)')

# eof