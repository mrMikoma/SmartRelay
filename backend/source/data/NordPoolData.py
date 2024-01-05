
from random import gauss
from nordpool import elspot
import math
from . import DateTime


def getNordPoolPrices(data):
    print(f"\nRetrieving electricity price data from Nordpool...")
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
        print(f'Time: {DateTime.dateDateString(price["start"])} price: {price["value"]} ', end='')
        # Handle data from Nordpool
        if price["value"] != float('inf'):
            data[DateTime.dateDateString(price["start"])] = {'Price': price["value"]}

        # Create random data if real data not available
        else:
            print("Created dummy data!")
            my_mean = 150
            my_variance = 250
            random_number = gauss(my_mean, math.sqrt(my_variance))
            data[DateTime.dateDateString(price["start"])] = {'Price': float("{:.2f}".format(random_number))}


    print(f"\n\nData retrieval completed.\n")
    return data

# eof