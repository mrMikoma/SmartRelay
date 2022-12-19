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

import NordPoolData
import FMIData


# MAIN
if __name__ == '__main__':
    # Starting program
    print(f'\nHi, this is a really simple application for controlling high current relay '
          + f'with Nordpool electricity price data\n')

    # Running program
    NordPoolData.getNordPoolPrices() # get electricity price data
    temperatures = FMIData.getFMItemperatures()
    FMIData.printTemperatures(temperatures)

    # Ending program
    print(f'\nThank you for using this program! :)')

# eof