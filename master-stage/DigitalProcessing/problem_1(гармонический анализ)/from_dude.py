import numpy as np
import matplotlib.pyplot as plt

A    = 2
tau  = .5
Tc   = .7

N    = 100

T    = .8
teta =  np.arange(0, T, T/N)

Wc   = 3000
W    = np.arange(0, Wc, Wc/N)

x    = np.zeros(N)

# def func(arg):
#   return A * np.exp(-arg / tau) if 0 < arg < T else 0

# x = np.array([func(t) for t in teta])

for i in range(N):

  x[i] = A * np.exp(-teta[i] / tau)

  if(teta[i] < 0 and teta[i] > T):
    x[i] = 0;


Xjw = []
Xw  = []
fi  = []
xv  = []


for i in range(N):
  
  # метод трапеций
  re = np.trapz(np.multiply(x, np.cos(teta * W[i])))
  im = np.trapz(np.sin(teta * W[i]), x=teta)
  Xjw.append(re + im * 1j)

  # print(Xjw[-1])

  Xw.append(np.abs(Xjw[-1]))
  fi.append(np.angle(Xjw[-1]))


for i in range(N):

  xv.append((1 / (2 * np.pi)) * np.trapz(np.multiply(Xjw, np.exp(np.multiply(W, teta[i] * 1j))), x=W))
  # xv(i) = (1/(2*pi))*trapz(W, Xjw.*exp(W.*teta(i)*1i))


plt.plot(W, xv)
plt.show()