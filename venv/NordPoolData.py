
from nordpool import elspot, elbas
from pprint import pprint
import json
import DateTime


def getNordPoolPrices():
    # Initialize class for fetching Elspot prices
    prices_spot = elspot.Prices()

    # Fetch hourly Elspot prices for Finland
    hourly = prices_spot.hourly(areas=['FI'])

    # Print the hourly dictionary
    #pprint(hourly)

    print(f'######################\n') # devider
    print(f'Daily details: ')

    # Print all keys and values
    for key, val in hourly.items():
        if key == "areas":
            continue

        else:
            print(key, val)

    print(f'######################\n') # devider
    print(f'Daily statistics: ')

    # Get area specific values
    areas = hourly.__getitem__('areas')
    statistic_prices = areas['FI']
    hourly_prices = statistic_prices['values']

    # Print statistic prices
    for key, val in statistic_prices.items():
        if key == "values":
            continue

        else:
            print(key, val)

    print("", end='')

    print(f'######################\n')  # devider
    print(f'Hourly prices: ')

    for price in hourly_prices:
        print(f'{price["value"]}; ', end='')

    print("", end='\n')


def getDate():
    print(DateTime.getCurrentDayDate())
    print(DateTime.getNextDayDate())

# eof