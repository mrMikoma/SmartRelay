import DummyData
import HandleData
import PlotData

# Declaring variables
data = {}
data_sum = []
numberOfTests = 1

for i in range(numberOfTests):
    # RETRIEVING DATA FROM APIs:
    # Electricity prices from NordPool
    # data = NordPoolData.getNordPoolPrices(data)    # get electricity price data
    data = DummyData.createDummyPriceData(data)  # for creating dummy data for testing purposes

    # Temperatures and wind speeds from FMI
    #data = FMIData.getFMIforecast(data)            # get FMI weather forecast data
    data = DummyData.createDummyWeatherData(data)   # for creating dummy data for testing purposes

    # HANDLING DATA
    data_sum.append(HandleData.offTime(data))

print(f'\n{data_sum}')
data_mean = sum(data_sum)/len(data_sum)
print(f'\nPOSSIBLE OFF TIME IS {float("{:.3f}".format(data_mean))}')

PlotData.plotHeatingPlan(data)