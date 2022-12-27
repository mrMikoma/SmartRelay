
"""
WIND CHILL LIMITING VARIABLES:
Formula from: https://www.weather.gov/media/epz/wxcalc/windChill.pdf

Temperature estimates (no wind):
# (-3.846) * float(str(windChill)) + 27.09  (1. version)
TEMPERATURE | WIND CHILL | OFF-TIME (1. version)
-25C       --> 7.04     --> 0h off   (min limit)
-15C       --> 5.83     --> 6h off   (~estimate)
-5C        --> 4.61     --> 12h off  (~estimate)
10C        --> 2.79     --> 18h off  (~estimate)
20C        --> 1.58     --> 21h off  (max limit)

#(-4.9383) * float(str(windChill)) + 34.7854 # (2. version)
TEMPERATURE | WIND CHILL | OFF-TIME (2. version)
-25C       --> 7.04     --> 0h off   (min limit)
-15C       --> 5.83     --> 6h off   (~estimate)
-5C        --> 4.61     --> 12h off  (~estimate)
10C        --> 2.79     --> 21h off  (max limit)
20C        --> 1.58     --> 21h off  (cut-off)
"""

import math
import DateTime

def calculateWindChill(T, V):
    windChill = (12.1452 + 11.6222 * math.sqrt(V) - 1.16222 * V) * (33 - T)
    return round((windChill/100), 3)

def calculateOffTime(windChill):
    offTime = (-4.9383) * float(str(windChill)) + 34.7854 # (2. version)



    return round(offTime, 3)

def windChillValues(tempList, windList):
    # Declaring variables
    windChillList = []

    # calculating wind chill
    for i in range(len(tempList)):
        x = calculateWindChill(tempList[i], windList[i])
        windChillList.append(float("{:.3f}".format(x)))

    return windChillList

def offTime(data):
    print(f'\nCalculating possible off time.')
    # Declaring varibles
    tempList = getValuesInList(data, 'Temperature')
    windList = getValuesInList(data, 'Wind speed')
    print(f'Temperatures: {tempList}')
    print(f'Wind speeds: {windList}')

    windChillList = windChillValues(tempList, windList)
    print(f'Wind chills: {windChillList}')

    offTime = calculateOffTime(float(sum(windChillList)/len(windChillList)))


    print(f'Mean wind chill value: {round(sum(windChillList)/len(windChillList), 2)}')
    print(f'Possible off time is: {round(offTime, 2)}')
    return round(offTime, 2)


def decideOffHours(data, offTime):
    print("aha")


    return

def getTimesInList(data):
    dates = data.keys()
    times = []
    for i in dates:
        times.append(DateTime.getTimeString(i))
    return times

def getValuesInList(data, key):
    data_list = []
    for i in data:
        data_list.append(data[i].get(key))
    return data_list

def printData(data):
    for i in data:
        print("Key : {} , Value : {}".format(i, data[i]))
    print("", end='\n')
    return

# eof