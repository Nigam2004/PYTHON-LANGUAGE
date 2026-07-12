# Syntax-plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, edgecolors=None, label=None)
# x, y:-Sequences of data points to plo
# s:-Marker size (scalar or array-like)
# c:-Marker color
# marker:-Shape of the marker
# cmap:-Colormap for mapping numeric values to colors
# alpha:-Transparency (0 = transparent, 1 = opaque)
# edgecolors:-Color of marker edges
# label:-Legend label for the dataset


import numpy as np
import matplotlib.pyplot as plt

x = np.array([12, 45, 7, 32, 89, 54, 23, 67, 14, 91])
y = np.array([99, 31, 72, 56, 19, 88, 43, 61, 35, 77])
x2 = np.array([150, 155, 160, 165, 170, 175, 180, 195, 200, 205])
y2 = np.array([50, 52, 54, 56, 58, 64, 66, 68, 70, 72])

plt.scatter(x,y,label="group1")
plt.scatter(x2,y2,label="group2")
plt.grid(True )
plt.legend()
plt.show()