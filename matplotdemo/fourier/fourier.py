import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

def draw(Z):
    im = ax.imshow(Z, interpolation='nearest', cmap='gray',
                   origin='lower', extent=[-2, 2, -2, 2],
                   vmax=abs(Z).max(), vmin=-abs(Z).max())

# Fixing random state for reproducibility
np.random.seed(19680801)

delta = 0.1
pixels = 512
x = y = np.linspace(-20.0, 20.0, pixels)
X, Y = np.meshgrid(x, y)
Z1 = np.sin(0.5*X*X)*np.sin(0.5*Y*Y)
Z1 = np.sin(X)
# Z1 = np.exp(-X**2 - Y**2)
# Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = Z1
print(Z)

Z2 = np.fft.fft2(Z)
print(Z2)
Z3 = np.real(Z2)
fig, ax = plt.subplots()
# im = ax.imshow(Z3, interpolation='nearest', cmap='gray',
#                origin='lower', extent=[0, 10, 0, 10],
#                vmax=abs(Z3).max(), vmin=-abs(Z3).max())

draw(Z3)

plt.show()