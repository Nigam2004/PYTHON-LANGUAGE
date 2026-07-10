# Syntax: plt.plot(x, y, color, linestyle, linewidth, marker)
# x: The values for the x-axis
# y: The corresponding values for the y-axis
# color: Specifies the color of the line
# linestyle: Defines the style of the line
# linewidth: Controls the thickness of the line
# marker: Adds markers at data points

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_axis=np.array([1,3,5,7])
y_axis=np.array([2,4,6,8])

plt.plot(x_axis,y_axis,color="red",linestyle="-",linewidth="1",marker="o")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line plot")
plt.show()