import numpy as np
import matplotlib.pyplot as plt

data=np.random.randn(100)
print(type(data))

plt.hist(data,bins=60,color="green",edgecolor="black")
plt.title("Basic histogram")
plt.show()