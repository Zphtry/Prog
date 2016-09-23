import matplotlib.pyplot as plt
import numpy as np


h_red = 1.054e-34

m = 9.1e-31

a = 3

U0 = 2

A1, B3, C = 1, 1, 1

alph = 0



def E(n):

	return ((np.pi * h_red * n / a) ** 2) / (2 * m)

def k1(n):

	return np.sqrt(2 * m * (U0 - E(n)) / (h_red ** 2))

def k2(n):

	return np.sqrt(2 * m* E(n) / (h_red ** 2))



def psi(x, n):

	if x < 0: return A1 * np.exp(k1(n) * x)

	if x > a: return B3 * np.exp(-k1(n) * x)

	return C * np.sin(k2(n) * x + alph)

x = np.arange(-1, 4.0, 0.1)

y = []

for i in x:
	
	y.append(psi(i,1))

plt.plot(x,y)
plt.grid(True)
plt.show()

	
