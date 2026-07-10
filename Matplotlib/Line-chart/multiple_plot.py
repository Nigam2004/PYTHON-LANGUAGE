import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([1, 2, 3, 4])
y = x * 2

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]

plt.plot(x,y,label="y=2-x")
plt.plot(x1,y1,"-",label='Second Line')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Multiple line on plot")
plt.grid(True)
plt.show()