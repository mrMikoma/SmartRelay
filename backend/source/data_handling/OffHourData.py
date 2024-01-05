import heapq
from . import HandleData, WindChillData
from ..data import DateTime


def decideOffHours(data, offHoursDict, offTime):
    # Declaring varibles
    pricesList = []

    # Deciding off hours
    for key in data:
        pricesList.append(data[key]['Price']) # data[key]['Price'])

    print(pricesList)


    #temp = heapq.nlargest(3, data.item, key=lambda i: i[1])

    ## ITERATE



    #print(temp)
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