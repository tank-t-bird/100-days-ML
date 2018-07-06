# Tank Thunderbird 100-days-ML Day 001-b-sine
# Since I am looking at vectors, I decided to look at matplotlib and plot a few.
# Sine

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10*np.pi, 0.1)     # start,stop,step
y = np.sin(x)
plt.plot(x,y)
plt.show()

