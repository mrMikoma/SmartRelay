# This is a simple Python script for controlling Shelly relay with
# Nordpool electricity price and FMI weather data.
# Author: @mrMikoma

# status: UNDER ACTIVE DEVELOPMENT

# Special thanks to
# - https://github.com/kipe/nordpool
# - https://github.com/pnuu/fmiopendata
# - https://github.com/Jan200101/ShellyPy
# -

"""
Improvement ideas:
- DO ALL :)
-
"""

import source.data.DummyData as DummyData
import source.data_handling.HandleData as HandleData
import source.data.NordPoolData as NordPoolData
import source.data.FMIData as FMIData
import source.data_handling.OffTimeData as OffTimeData
import source.data_handling.PlotData as PlotData

# MAIN
if __name__ == '__main__':
    # Program startup
    print(f'\nHi, this is a simple Python script for controlling Shelly relay '
          + f'with Nordpool electricity price and FMI weather data.\n')

    # Declaring variables
    data = {}

    # RETRIEVING DATA:
    # Electricity prices from NordPool
    #data = NordPoolData.getNordPoolPrices(data)    # get electricity price data
    data = DummyData.createDummyPriceData(data)     # for creating dummy data for testing purposes
    #HandleData.printData(data)

    # Temperatures and wind speeds from FMI
    data = FMIData.getFMIforecast(data)             # get FMI weather forecast data
    #data = DummyData.createDummyWeatherData(data)   # for creating dummy data for testing purposes
    HandleData.printData(data)

    # HANDLING DATA
    # Optimize off-hours
    #offTime = MinMaxOptimazation.offTime()         # WIP
    offTime = OffTimeData.offTime(data)
    #offHours = OffTimeData.decideOffHours(data, offTime)

    # Plotting data for data visualization
    PlotData.plotPrice(data)
    PlotData.plotWeather(data, offTime)

    # Controlling relay (to be added)


    # Ending program
    print(f'\nThank you for using this program! :)')

# eof