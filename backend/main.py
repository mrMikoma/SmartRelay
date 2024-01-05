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

import source.utility.Menu as Menu
import source.data.DummyData as DummyData
import source.data_handling.HandleData as HandleData
import source.data.NordPoolData as NordPoolData
import source.data.FMIData as FMIData
import source.data_handling.OffTimeData as OffTimeData
import source.data_handling.OffHourData as OffHourData
import source.data_handling.PlotData as PlotData

# MAIN
if __name__ == '__main__':
    # Program startup
    print(f'\nHi, this is a simple Python script for controlling Shelly relay '
          + f'with Nordpool electricity price and FMI weather data.')

    # Declaring variables
    data = {}
    offTime = 0

    while True:
        # Getting user input
        Menu.printMenu()
        userInput = input(f'Select option (0 = exit): ')
        print(f'')

        # Handling user input
        if userInput == '0':
            break
        elif userInput == '1':
            data = NordPoolData.getNordPoolPrices(data)
            continue
        elif userInput == '2':
            data = DummyData.createDummyPriceData(data)
            continue
        elif userInput == '3':
            data = FMIData.getFMIforecast(data)
            continue
        elif userInput == '4':
            data = DummyData.createDummyWeatherData(data)
            continue
        elif userInput == '5':
            #offTime = MinMaxOptimazation.offTime()                 # WIP
            offTime = OffTimeData.offTime(data)
            continue
        elif userInput == '6':
            offHours = OffHourData.decideOffHours(data, offTime)    # WIP
            continue
        elif userInput == '7':
            HandleData.printData(data)
            continue
        elif userInput == '8':
            PlotData.plotPrice(data)
            continue
        elif userInput == '9':
            PlotData.plotWeather(data, offTime)
            continue
        elif userInput == '10':
            PlotData.plotHeatingPlan(data)                          # WIP
            continue
        elif userInput == '11':
            print(f'Controlling relay (WIP)')                       # WIP
            continue
        else:
            print(f'Invalid input!')

    # Ending program
    print(f'\nThank you for using this program! :)')

# eof