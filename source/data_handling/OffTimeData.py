#import heapq
from math import floor

from data_handling.HandleData import *
from data_handling.WindChillData import *

def calculateOffTime(temperatureList, windSpeedList):
    # Declaring variables
    tempetatureMean = sum(temperatureList) / len(temperatureList)
    windSpeedMean = sum(windSpeedList) / len(windSpeedList)

    # Calculatin offtime
    offTime = 0.45 * tempetatureMean - 0.65 * windSpeedMean + 11.3
    return round(offTime, 3)

def offTime(data):
    print(f'\nCalculating possible off time.')
    # Declaring varibles
    tempList = getValuesInList(data, 'Temperature')
    windList = getValuesInList(data, 'Wind speed')
    print(f'Temperatures: {tempList}')
    print(f'Wind speeds: {windList}')

    windChillList = windChillValues(tempList, windList)
    print(f'Wind chills: {windChillList}')

    offTime = calculateOffTime(tempList, windList)


    print(f'Mean wind chill value: {round(sum(windChillList)/len(windChillList), 2)}')
    print(f'Possible off time is: {round(offTime, 2)}')
    return round(offTime, 0)

def decideOffHours(data, offHoursDict, offTime):
    # Declaring varibles
    pricesList = []



    # Deciding off hours
    for key in data:
        pricesList.append(data[key]['Price']) # data[key]['Price'])

    print(pricesList)

    temp = heapq.nlargest(3, data.item, key=lambda i: i[1])

    ## ITERATE


    # heapq.nlargest(3, fruitCount.items(), key=lambda i: i[1])


    print(temp)


    return offHoursDict
def offHours(data, offTime):
    # Declaring variables
    offHoursDict = initializeOffHourStructure(data)

    # Deciding off hours
    offHoursDict = decideOffHours(data, offHoursDict, offTime)


    # Setting data into data structure
    data = settingCorrectData(data, offHoursDict)

    print(f"Off hours decided!")
    return data

def initializeOffHourStructure(data):
    # Declaring variables
    i = 0
    res = dict()
    offHoursList = [False for _ in range(len(data))]

    # Declaring testing dictionary with time and status values
    for key in data:
        res[DateTime.dateStringDate(key)] = offHoursList[i]
        i += 1

    # printing result
    print("The constructed Dictionary : " + str(res))
    return res

def settingCorrectData(data, offHoursDict):
    # Setting off hours into data structure
    for key in offHoursDict:
        if DateTime.dateDateString(key) in data:
            data[DateTime.dateDateString(key)].update({
                'RelayOn': offHoursDict[key]
            })

    return data

# eof