import DateTime

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