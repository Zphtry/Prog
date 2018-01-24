import numpy as np
import matplotlib.pyplot as plt

from f import F
from r import R
from ma import MA
from ols import OLS
from mofd import MoFD
from em import EM

N = 200
w = np.arange(0, N)

x = F(N)
r = R(N)
y = x + r

plt.plot(w, x)
plt.show()

plt.plot(w, r)
plt.show()

plt.plot(w, y)
plt.show()


L = [2, 4, 6, 8]


MovAve = np.zeros((len(L), N))

for i in range(len(L)):
  MovAve[i, :] = MA(y, L[i])
    # MovAve(i,:) = MA(y,L(i))
  plt.plot(w, MovAve[i,:])
  plt.show()


MovAveOLS = np.zeros(len(L))
for n in range(len(L)):
  MovAveOLS[n] = OLS(MovAve[n,:], x)

print(MovAveOLS)

M2 = MoFD(y)
M2OLS = OLS(M2,x)
print(M2OLS)

plt.plot(w, M2)
plt.show()

a = np.arange(.1, .9, .1)

M3 = np.zeros((len(a), N))
for i in range(len(a)):
  M3[i, :] = EM(y, a[i])
  plt.plot(w, M3[i,:])
  plt.show()

M3OLS = np.zeros(len(a))
for n in range(len(a)):
  M3OLS[n] = OLS(M3[n, :], x)

print(M3OLS)

plt.plot(a, M3OLS)
plt.show()
