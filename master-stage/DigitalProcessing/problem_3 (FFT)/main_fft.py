import numpy as np
import matplotlib.pyplot as plt

from func import Func
from dft_part import dft_exp
from fft import FFT

N  = 128
Tc = 1.5
Wc = 200

Q  = np.linspace(0, Tc - 1e-5, N)
F  = np.linspace(0, Wc - 1e-5, N)

y = np.zeros(len(Q))
for i in range(len(Q)):
    y[i] = Func(Q[i])

plt.plot(Q,y)
plt.show()


Sw = np.zeros(len(F))
for k in range(len(F)):
  for n in range(len(F)):
    Sw[k] += y[n] * dft_exp(k - 1, n - 1, N)



plt.plot(F, np.abs(Sw), np.angle(Sw))
# plt.plot(F, np.abs(Sw), np.abs(FFT(y)))
plt.show()
plt.show()

# Sdft = DFT(y);


# F1 = 0:Wc/length(Sdft):Wc - 0.00001;
# figure(2);
# subplot(1,2,1);
# plot(F, abs(Sw));
# subplot(1,2,2);
# figure(2);
# plot(F, abs(Sdft));

# Err = abs(Sw - Sdft);
# P = max(Err);
# MaxErr = max(Err)/max(abs(Sw));
# disp(MaxErr);