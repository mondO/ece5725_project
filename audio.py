import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from scipy import signal as sig

volume = 1     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
sine = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
print("playing test sine wave")
sd.play(sine, fs)
sd.wait()

signal = np.loadtxt('guitar.txt')
# signal[signal > 100]
signal = signal - np.mean(signal)
print(signal.shape)
resampled = sig.resample(signal, int(fs/11888) * len(signal))
print(resampled.shape)
plt.plot(signal)
plt.show()

sd.play(resampled, fs)
sd.wait()
