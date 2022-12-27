
import matplotlib.pyplot as plt
import numpy as np
import DateTime
import HandleData


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
       windChills = HandleData.windChillValues(temperatures, windSpeeds)


       # plot
       plt.plot(times, temperatures, label="Temperatures (Celsius)")
       plt.plot(times, windSpeeds, label="Wind speeds (m/s)")
       plt.plot(times, windChills, label="Wind chill (W/m²)")


       plt.ylabel('weather')
       plt.xlabel('time')
       plt.grid(True)
       plt.legend()
       plt.show()
       return

def plotHeatingPlan(raw_data):
       # Declare variables
       temperatures = range(-25, 30, 5)
       windSpeed = 0
       offHours = []

       # Get data (windSpeed = 0)
       for t in temperatures:
              windChill = HandleData.calculateWindChill(t, windSpeed)
              offHours.append(HandleData.calculateOffTime(windChill))

       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeed}m/s')

       # Get data (windSpeed = 2.5)
       offHours.clear()
       windSpeed = 2.5
       for t in temperatures:
              windChill = HandleData.calculateWindChill(t, windSpeed)
              offHours.append(HandleData.calculateOffTime(windChill))

       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeed}m/s')

       # Get data (windSpeed = 5)
       offHours.clear()
       windSpeed = 5
       for t in temperatures:
              windChill = HandleData.calculateWindChill(t, windSpeed)
              offHours.append(HandleData.calculateOffTime(windChill))

       plt.plot(temperatures, offHours, label=f'Off (h), windSpeed={windSpeed}m/s')

       # plot config
       plt.ylabel('Off Hours (h)')
       plt.xlabel('Temperature (C)')
       plt.grid(True)
       plt.legend()
       plt.show()
       return
# eof