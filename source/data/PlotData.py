import matplotlib.pyplot as plt

import DateTime


def plotPrice(raw_data):
       # Declare variables
       plt.style.use('ggplot')

       # Times and prices
       dates = raw_data.keys()
       times = []
       prices = []

       for i in dates:
              times.append(DateTime.getTimeString(i))
              prices.append(raw_data[i].get('Price'))

       # plot
       plt.plot(times, prices, label="Elspot price")
       plt.ylabel('price')
       plt.xlabel('time')
       plt.legend()
       plt.show()
       return

def plotWeather(raw_data):
       # Declare variables
       plt.style.use('ggplot')

       # Times and prices
       dates = raw_data.keys()
       times = []
       temperatures = []
       windSpeeds = []
       for i in dates:
              times.append(DateTime.getTimeString(i))
              temperatures.append(raw_data[i].get('Temperature'))
              windSpeeds.append(raw_data[i].get('Wind speed'))

       # plot
       plt.plot(times, temperatures, label="Temperatures")
       plt.plot(times, windSpeeds, label="Wind speeds")
       plt.ylabel('weather')
       plt.xlabel('time')
       plt.legend()
       plt.show()
       return