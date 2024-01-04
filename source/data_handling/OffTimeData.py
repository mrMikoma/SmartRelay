from . import HandleData, WindChillData
from ..data import DateTime

def calculateOffTime(temperatureList, windSpeedList):
    # Declaring variables
    tempetatureMean = sum(temperatureList) / len(temperatureList)
    windSpeedMean = sum(windSpeedList) / len(windSpeedList)

    # Calculatin offtime
    offTime = 0.45 * tempetatureMean - 0.65 * windSpeedMean + 11.3

    # Handling limits
    if offTime < 0:
        offTime = 0 
    elif offTime > 21:
        offTime = 21

    return round(offTime, 3)

def offTime(data):
    print(f'\nCalculating possible off time.')

    # Declaring varibles
    tempList = HandleData.getValuesInList(data, 'Temperature')
    windList = HandleData.getValuesInList(data, 'Wind speed')
    windChillList = WindChillData.windChillValues(tempList, windList)

    # Printing values
    print(f'Temperatures: {tempList}')
    print(f'Wind speeds: {windList}')
    print(f'Wind chills: {windChillList}')

    # Calculating off time
    offTime = calculateOffTime(tempList, windList)

    # Printing results
    print(f'Mean wind chill value: {round(sum(windChillList)/len(windChillList), 2)}')
    print(f'Possible off time is: {round(offTime, 2)}')
    return round(offTime, 0)

# eof