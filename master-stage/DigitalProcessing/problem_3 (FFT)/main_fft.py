import numpy as np
import matplotlib.pyplot as plt

from func import Func
from w import W

N  = 128
Tc = 1.5
Wc = 200

Q  = np.linspace(0, Tc - .00001, N)
F  = np.linspace(0, Wc - .00001, N)

y = np.zeros(len(Q))
for i in range(len(Q)):
    y[i] = Func(Q[i])

Sw = np.zeros(len(F))
for k in range(len(F)):
  for n in range(len(F)):
    Sw[k] += y[n] * W(k - 1, n - 1, N)

# plt.plot(Q,y)


# plt.plot(F, np.real(Sw), np.imag(Sw))
plt.plot(F, np.imag(Sw))
plt.show()

Sdft = DFT(y);

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