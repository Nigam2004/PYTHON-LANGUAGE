# Syntax: plt.bar(x, height, width, bottom, align)

import numpy as np
import matplotlib.pyplot as plt

fruits=["banana","aple","guava","orange"]
sales=[600,700,300,468]
print(type(sales))

plt.bar(fruits,sales,color="green")
plt.xlabel("Fruits name",color="red")
plt.ylabel("sales data")
plt.title("fruits sales Data")
plt.show()