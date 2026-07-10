import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_axis=np.array([1,3,5,7])
y_axis=np.array([2,4,6,8])
print(x_axis)
plt.plot(x_axis,y_axis,marker="o")
for x1,y1 in zip(x_axis,y_axis): 
    print(x1,y1)
    plt.annotate(f"({x1},{y1})",(x1,y1))   ## annotation
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("line plot with annotation")
plt.grid(True)
plt.show()