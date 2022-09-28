# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.resample.html

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(x**2/6.0)
y1 = signal.resample(y, 100)
x1 = np.linspace(0, 10, 100, endpoint=False)
plt.plot(x,y, 'go-', x1, y1, 'o--')
plt.show()

