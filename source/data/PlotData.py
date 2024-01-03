
import matplotlib.pyplot as plt
from data_handling import WindChillData, OffTimeData, HandleData


def plotPrice(raw_data):
       # Declare variables
       times = HandleData.getTimesInList(raw_data)
       prices = HandleData.getValuesInList(raw_data, 'Price')
       print(prices)

       # plot
       plt.plot(times, prices, label="Elspot price (EUR/MWh)")
       plt.ylabel('price')
       plt.xlabel('time')
       plt.grid(True)
       plt.legend()
       plt.show()
       return

def plotWeather(raw_data, offTime):
       # Declare variables
       times = HandleData.getTimesInList(raw_data)
       temperatures = HandleData.getValuesInList(raw_data, 'Temperature')
       windSpeeds = HandleData.getValuesInList(raw_data, 'Wind speed')
       windChills = WindChillData.windChillValues(temperatures, windSpeeds)


       # plot
       plt.plot(times, temperatures, label="Temperatures (Celsius)")
       plt.plot(times, windSpeeds, label="Wind speeds (m/s)")
       plt.plot(times, windChills, label="Wind chill (W/m²) / 100")


       plt.ylabel('weather')
       plt.xlabel('time')
       plt.grid(True)
       plt.legend()
       plt.show()
       return

def plotHeatingPlan(raw_data):
       # Declare variables
       temperatures = [i for i in range(-25,30,5)]
       offHours = []

       # Get data (windSpeed = 0)
       windSpeeds = 0
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Get data (windSpeed = 1)
       offHours.clear()
       windSpeeds = 1
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Get data (windSpeed = 2.5)
       offHours.clear()
       windSpeeds = 2.5
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Get data (windSpeed = 5)
       offHours.clear()
       windSpeeds = 5
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Get data (windSpeed = 7.5)
       offHours.clear()
       windSpeeds = 7.5
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Get data (windSpeed = 10)
       offHours.clear()
       windSpeeds = 10
       for i in temperatures:
              offHours.append(OffTimeData.calculateOffTime([i], [windSpeeds]))
       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeeds}m/s')

       # Plot 0h line
       offHours = [0 for _ in range(len(temperatures))]
       plt.plot(temperatures, offHours, label=f'0h off line', color="red")

       # Plot 21h line
       offHours = [21 for _ in range(len(temperatures))]
       plt.plot(temperatures, offHours, label=f'21h off line', color="green")

       # plot config
       plt.ylabel('Off Hours (h)')
       plt.xlabel('Temperature (C)')
       plt.grid(True)
       plt.legend()
       plt.show()
       return
# eof