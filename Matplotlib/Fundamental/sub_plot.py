import numpy as np
import matplotlib.pyplot as plt
fig,ax = plt.subplots(3, 3)
print(ax)
for row in ax:
    for col in row:
        col.plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))

plt.show()