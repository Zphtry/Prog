import matplotlib.pyplot as plt
import numpy as np

h = 6.582e-16

m = 9.1e-31

a = 2

k = 1

U0_beg = -5

U0_end = 5 


def q(U0):

	return np.sqrt(k ** 2 + U0 * 2 * m / (h ** 2) + 0j)

def C_pl(U0):

	return -q(U0) * a * np.tan(q(U0) * a) / (1j * k * a)

def C_mi(U0):

	return q(U0) * a / (1j * k * a * np.tan(q(U0) * a))

def t(U0):

	return np.exp(-2j * k * a) * ((C_pl(U0) + 1) / (C_pl(U0) - 1) - (C_mi(U0) + 1) / (C_mi(U0) - 1)) / 2

def D(U0):

	return abs(t(U0)) ** 2

X = np.arange(U0_beg, U0_end, 0.001)

Y = []

for x in X:

	Y.append(D(x))


Y = D(X)

plt.plot(X, Y)

plt.show()




