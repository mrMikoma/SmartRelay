
import math
from random import gauss
from . import DateTime


def createDummyPriceData(data):
    print(f'Creating dummy data for Nordpool prices...')
    # Declaring variables
    date = DateTime.getCurrentDayDate()
    date = DateTime.getHoursFrom(date, 0)
    my_mean = 150
    my_variance = 250

    # Creating random variables
    for i in range(24):
        random_number = gauss(my_mean, math.sqrt(my_variance))
        data[DateTime.getHoursFrom(date, i)] = {'Price': float("{:.2f}".format(random_number))}

    print(f"Data creating completed.")
    return data


def createDummyWeatherData(data):
    print(f'Creating dummy data for weather variables...')
    # Declaring variables
    # Temperature variables
    my_mean = -5
    my_variance = 0

    # Creating random temperatures
    for x in data:
        random_number = gauss(my_mean, math.sqrt(my_variance))
        data[x].update({'Temperature': float("{:.1f}".format(random_number))})

    # Wind speed variables
    my_mean = 0
    my_variance = 0

    # Creating random wind speed
    for x in data:
        random_number = gauss(my_mean, math.sqrt(my_variance))
        data[x].update({'Wind speed': abs(float("{:.2f}".format(random_number)))})

    print(f"Data creating completed.")
    return data

# eof