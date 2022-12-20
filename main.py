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
import WindyData


# MAIN
if __name__ == '__main__':
    # Starting data
    print(f'\nHi, this is a really simple application for controlling high current relay '
          + f'with Nordpool electricity price data.\n')

    # Retrieving data (WORKING)
    #NordPoolData.getNordPoolPrices() # get electricity price data
    data = FMIData.getFMIforecast()
    FMIData.printData(data)


    # Ending data
    print(f'\nThank you for using this program! :)')

# eof