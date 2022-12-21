# This is a simple Python script for controlling high current relay with
# Nordpool electricity price data.

# status: UNDER ACTIVE DEVELOPMENT

# Author @mrMikoma

# Thanks to
# - https://github.com/kipe/nordpool
# - https://github.com/pnuu/fmiopendata
# - https://github.com/Jan200101/ShellyPy


"""
Improvement ideas:
- DO ALL :)
-
"""

import FMIData
import NordPoolData
import PlotData
import WindyData


# MAIN
if __name__ == '__main__':
    # Starting data
    print(f'\nHi, this is a really simple application for controlling high current relay '
          + f'with Nordpool electricity price data.\n')

    # Retrieving data (WORKING)
    data = {}

    data = NordPoolData.getNordPoolPrices(data)    # get electricity price data
    #data = NordPoolData.createDummyData(data)     # for creating dummy data for testing purposes
    FMIData.printData(data)

    data = FMIData.getFMIforecast(data)            # get FMI weather forecast data
    FMIData.printData(data)

    # Handle data
    PlotData.plotPrice(data)
    PlotData.plotWeather(data)

    # Ending data
    print(f'\nThank you for using this program! :)')

# eof