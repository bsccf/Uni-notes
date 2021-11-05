import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(0, 1)
y = np.exp(-x) * np.sin(4*np.pi * x)
plt.plot( x, y )

print("")
