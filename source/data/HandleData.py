import matplotlib.pyplot as plt
import numpy as np


def plotData(raw_data):
       # Declare variables
       plt.style.use('ggplot')
       x = ''.join(raw_data.keys())
       y = 4 + 2 * np.sin(2 * x)

       # plot
       plt.plot(x)
       plt.ylabel('some numbers')
       plt.xlabel('time')
       plt.show()
       return