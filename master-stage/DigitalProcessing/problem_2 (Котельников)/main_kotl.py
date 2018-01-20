import numpy as np
import matplotlib.pyplot as plt

from cdf     import CDF
from func    import _func
from fourier import _fourier


N   = 800

T   = 1
Tc  = 1

omc  = 100

t  = np.linspace(0, Tc, N)
om = np.linspace(0, omc, N)

n = 7

Fi = CDF(t, T, n)

fou = _fourier(Fi, t, om)

# plt.plot(t, np.real(fou))
# plt.plot(t, np.imag(fou))




# x = np.zeros(N)
# A, tau = 2, .5
# for i in range(N):
#   x[i] = A * np.exp(-t[i] / tau) if 0 <= t[i] < Tc else 0

func = _func(t)
plt.plot(t, _func)

plt.show()
exit()

# амплитудная характеристика
Xw = np.zeros(N)
for i in range(N):
  re = np.trapz(np.multiply(x, np.cos(t * om[i])), x=t)
  im = np.trapz(np.multiply(x, np.sin(t * om[i])), x=t)
  Xw[i] = np.sqrt(re ** 2 + im ** 2)
# plt.plot(om, Xw)



maxXw = .05 * max(Xw)
for i in range(N):
   if Xw[i] <= maxXw:
       omv = om[i]

print(omv)


T = np.pi / omv
NN = int(np.fix(Tc / T))
t1 = np.arange(0, Tc, T / 900)


x1 = np.zeros(len(t1))

for i in range(len(t1)):
  x1[i] = A * np.exp(-t1[i] / tau) if 0 <= t1[i] < Tc else 0

# plt.plot(t1, x1)
plt.plot(t1, x1)
plt.show()

Xn1 = np.zeros(len(t1))
for i in range(len(t1)):
  for nn in range(NN + 1):
        Xn1[i] += _func(T * (nn - 1), Tc) * CDF(t1[i], T, nn - 1)


plt.plot(t1, Xn1)
plt.show()

# figure(5);
# subplot(1,2,1);
# plot(t1,x1);
# subplot(1,2,2);
# plot(t1,Xn1);

# err = abs(x1 - Xn1);
# MaxEps = max(err);
# disp(MaxEps);

# figure(6);
# plot(t1,err);
