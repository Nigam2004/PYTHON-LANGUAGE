# Syntax-plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, edgecolors=None, label=None)
import numpy as np
import matplotlib.pyplot as plt

x = np.array([12, 45, 7, 32, 89])
y = np.array([99, 31, 72, 56, 19])
a=["green","red","yellow","pink","black"] #color
b=[20,43,56,89,200]# size
plt.scatter(x,y,s=b,c=a,alpha=1,edgecolors='blue',cmap="viridis", linewidths=1,marker="*")
plt.colorbar(label="color bar")
plt.title("Scatter Plot with Varying Colors and Sizes")
plt.show()