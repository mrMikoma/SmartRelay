# This is a simple Python script for controlling high current relay with
# Nordpool electricity price data.

# status: UNDER ACTIVE DEVELOPMENT

# Author @mrMikoma

# Thanks to
# - https://github.com/kipe/nordpool


"""
Improvement ideas:
- DO ALL :)
-
"""

import FMIData
import NordPoolData


# MAIN
if __name__ == '__main__':
    # Starting data
    print(f'\nHi, this is a really simple application for controlling high current relay '
          + f'with Nordpool electricity price data\n')

    # Running data
    NordPoolData.getNordPoolPrices() # get electricity price data
    temperatures = FMIData.getFMItemperatures()
    FMIData.printTemperatures(temperatures)

    # Ending data
    print(f'\nThank you for using this program! :)')

# eof