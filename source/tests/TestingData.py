
import DummyData
from data_handling import OffTimeData, HandleData

# Declaring variables
data = {}
numberOfTests = 1

for i in range(numberOfTests):
    # RETRIEVING DATA FROM APIs:
    data.clear()
    # Electricity prices from NordPool
    # data = NordPoolData.getNordPoolPrices(data)    # get electricity price data
    data = DummyData.createDummyPriceData(data)  # for creating dummy data for testing purposes

    # Temperatures and wind speeds from FMI
    #data = FMIData.getFMIforecast(data)            # get FMI weather forecast data
    data = DummyData.createDummyWeatherData(data)   # for creating dummy data for testing purposes

    # HANDLING DATA
    offTime = OffTimeData.offTime(data)
    data = OffTimeData.offHours(data, offTime)

# Print results
print(f'AND OFF HOURS ARE:')
HandleData.printData(data)
print(f'\nPOSSIBLE OFF TIME IS {offTime}')

# Plot results
#PlotData.plotHeatingPlan(data)