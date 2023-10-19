import numpy as np
import matplotlib.pyplot as plt

A = 1
omega = 100 * np.pi
T = 2 * np.pi / omega
f = 1 / T
psi = 1 / 4 * np.pi

t = np.linspace(0, 2 * T, 1000)

f_t = A * np.sin(omega * t + psi)

plt.figure(figsize=(8, 4))
plt.plot(t, f_t, label=f'sin({omega}t + {psi})', color='blue')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.title('Wykres sygnału sinusoidalnego')
plt.grid(True)
plt.show()
