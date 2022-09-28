# https://realpython.com/python-scipy-fft/

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft


SAMPLE_RATE = 128 # Hertz
DURATION = 8 # Seconds
SCALE = 512/SAMPLE_RATE

def sampler_fun(fun, sample_rate, duation, scale=1):
    x = np.linspace(0, duation, sample_rate*duation, endpoint=False)
    y = fun(x)
    
    xx = np.linspace(0, duation, sample_rate*duation*scale, endpoint=False)
    y1, y2 = np.meshgrid(np.linspace(0,1,scale), y)

    yy = y2.reshape(y2.shape[0]*y2.shape[1])
    return xx, yy



def fun0(x):
    return np.sin(2*np.pi*x*x)

x, y = sampler_fun(fun0, SAMPLE_RATE, DURATION,int(SCALE))
plt.plot(x, y)
plt.show()

# xx = np.linspace(0, duation, )

N = SAMPLE_RATE * DURATION * int(SCALE)
yf = rfft(y)
xf = rfftfreq(N, 1 / SAMPLE_RATE / SCALE)
#
plt.plot(xf, np.abs(yf))
plt.show()