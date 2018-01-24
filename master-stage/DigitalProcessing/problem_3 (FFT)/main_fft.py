import numpy as np
import matplotlib.pyplot as plt

from func import Func
from dft_part import dft_exp
from fft import FFT

N  = 512
Tc = 1.5
Wc = 200

Q  = np.linspace(0, Tc, N)
F  = np.linspace(0, Wc, N)

#function
y = Func(Q)

plt.plot(Q, y)
plt.title('Исходная функция')
plt.savefig('origin.png')
plt.show()

Sw = np.array([0+0j] * N)

for k in range(len(F)):
  for n in range(len(F)):
    Sw[k] += y[n] * dft_exp(k, n, N)


plt.plot(F, np.real(Sw))
plt.plot(F, np.imag(Sw))
plt.title('DFT')
plt.savefig('dft.png')
plt.show()


Sdft = FFT(y);
plt.plot(np.real(Sdft))
plt.plot(np.imag(Sdft))
plt.savefig('fft.png')
plt.title('FFT')
plt.show()


Err = abs(Sw - Sdft);
plt.plot(Err)
plt.savefig('err.png')
plt.show()
