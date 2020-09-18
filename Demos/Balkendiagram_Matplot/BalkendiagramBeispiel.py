# Balkendiagramm mit MathPlot

import matplotlib.pyplot as plt

XAchse = [1,2,3,4]
YAchse = [100,300,240,400]
bars = plt.bar(XAchse, YAchse)
bars[0].set_color('red')
plt.show()