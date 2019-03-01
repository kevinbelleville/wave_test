import numpy as np
import matplotlib.pyplot as plt

N = 1100
T = 1.0/800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5*np.sin(80.0 * 2.0 * np.pi * x)
yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# plt.plot(x, y)
plt.show()
