import numpy as np
import matplotlib.pyplot as plt

from cdf import CDF
from func import Func


N   = 800

T   = 1
Tc  = 1

Wc  = 100

# teta = 0:Tc/N:Tc
# W    = 0:Wc/N:Wc
teta = np.linspace(0, Tc, N)
W    = np.linspace(0, Wc, N)

n = 7

Fi = np.zeros(N)

for i in range(N):

  if (teta[i] == n * T):
      Fi[i] = 1

  else:
      Fi[i] = np.sin((np.pi / T) * (teta[i] - n * T)) / ((np.pi / T) * (teta[i] - n * T))

Xjw = []

for i in range(N):
  # метод трапеций
  re = np.trapz(np.multiply(Fi, np.cos(teta * W[i])), x=teta)
  im = np.trapz(np.multiply(Fi, np.sin(teta * W[i])), x=teta)
  Xjw.append(re + im * 1j)

x = np.zeros(N)
A, tau = 2, .5
for i in range(N):
  x[i] = A * np.exp(-teta[i] / tau) if 0 <= teta[i] < Tc else 0


# амплитудная характеристика
Xw = np.zeros(N)
for i in range(N):
  re = np.trapz(np.multiply(x, np.cos(teta * W[i])), x=teta)
  im = np.trapz(np.multiply(x, np.sin(teta * W[i])), x=teta)
  Xw[i] = np.sqrt(re ** 2 + im ** 2)
# plt.plot(W, Xw)



maxXw = .05 * max(Xw)
for i in range(N):
   if Xw[i] <= maxXw:
       Wv = W[i]

print(Wv)


T = np.pi / Wv
NN = int(np.fix(Tc / T))
teta1 = np.arange(0, Tc, T / 900)


x1 = np.zeros(len(teta1))

for i in range(len(teta1)):
  x1[i] = A * np.exp(-teta1[i] / tau) if 0 <= teta1[i] < Tc else 0

# plt.plot(teta1, x1)
plt.plot(teta1, x1)
plt.show()

Xn1 = np.zeros(len(teta1))
for i in range(len(teta1)):
  for nn in range(NN + 1):
        Xn1[i] += Func(T * (nn - 1), Tc) * CDF(teta1[i], T, nn - 1)


plt.plot(teta1, Xn1)
plt.show()

# figure(5);
# subplot(1,2,1);
# plot(teta1,x1);
# subplot(1,2,2);
# plot(teta1,Xn1);

# err = abs(x1 - Xn1);
# MaxEps = max(err);
# disp(MaxEps);

# figure(6);
# plot(teta1,err);
