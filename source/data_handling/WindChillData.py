
import math


"""
WIND CHILL LIMITING VARIABLES:
Formula from: https://www.weather.gov/media/epz/wxcalc/windChill.pdf

Temperature estimates (no wind):
TEMPERATURE | WIND CHILL | OFF-TIME (1. version)
-25C       -->          --> 0h off   (min limit)
-15C       -->          --> 6h off   (~estimate)
-5C        -->          --> 12h off  (~estimate)
10C        -->          --> 18h off  (~estimate)
21.5C      -->          --> 21h off  (max limit)


"""

def calculateWindChill(T, V):
    windChill = (12.1452 + 11.6222 * math.sqrt(V) - 1.16222 * V) * (33 - T)
    return round((windChill/100), 3)

def windChillValues(tempList, windList):
    # Declaring variables
    windChillList = []

    # calculating wind chill
    for i in range(len(tempList)):
        x = calculateWindChill(tempList[i], windList[i])
        windChillList.append(float("{:.3f}".format(x)))

    return windChillList

# eof