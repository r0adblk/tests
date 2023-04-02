import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5*np.e,512)
y = np.exp(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()