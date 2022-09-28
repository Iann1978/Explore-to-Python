# https://realpython.com/python-scipy-fft/

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft


SAMPLE_RATE = 44100 # Hertz
DURATION = 5 # Seconds

def generate_sin_wave(freq, sample_rate, duation):
    x = np.linspace(0, duation, sample_rate*duation, endpoint=False)
    frequencies = x * freq
    y = np.sin(2*np.pi*frequencies)
    return x, y

x, y = generate_sin_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()

_, nice_tone = generate_sin_wave(400, SAMPLE_RATE, DURATION)
_, noice_tone = generate_sin_wave(4000, SAMPLE_RATE, DURATION)
noice_tone = noice_tone * 0.2
mix_tone = nice_tone + noice_tone

plt.plot(x[:1000],mix_tone[:1000])
plt.show()


N = SAMPLE_RATE * DURATION
yf = rfft(mix_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()

# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (SAMPLE_RATE / 2)
# Our target frequency is 4000 Hz
target_idx = int(points_per_freq * 4000)
yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf))
plt.show()


new_sig = irfft(yf)
plt.plot(x[:1000], new_sig[:1000])
plt.show()