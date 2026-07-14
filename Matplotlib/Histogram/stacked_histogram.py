import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(1, 1, 500)
print(data1)
plt.hist([data1, data2], bins=15, stacked=True, label=['Category A', 'Category B'],edgecolor="black")
plt.legend()
plt.show()