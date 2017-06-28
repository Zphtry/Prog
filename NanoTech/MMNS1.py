import matplotlib.pyplot as plt
import numpy as np

eps, eps2 = 0.001, 0.01
U0        = 2
m         = 9.1e-31
h         = 6.582e-16
a         = 3
k0        = np.sqrt(U0 * 2 * m / (h ** 2))

evn_len,   odd_len   = 0, 0
k_evn,     k_odd     = [], []
cap_evn,   cap_odd   = [], []
A,         B         = [], []
x_evn,     y_evn     = [], []
x_odd,     y_odd     = [], []
listU_evn, listU_odd = [], []

def f(x): 
	return np.tan(a * x) + sign * np.sqrt(k0 ** 2 - x ** 2) / x
def bisection_method(l, r):
	bis = 0
	l += eps

	while r - l > eps:
		bis = (l + r) / 2
		if   (f(l) * f(bis) < 0): r = bis
		elif (f(r) * f(bis) < 0): l = bis;
		else: return  0

	return bis
def sol():
	T    = np.pi / a
	l, r =  T / 2, T
	X    = []
	if sign < 0: l, r = 0, T / 2

	while True:
		x = bisection_method(l, r)
		if x == 0: break
		X.append(x)
		l += T
		r += T

	return X
def cap_calc():

	for i in range(0, len(k_evn)): cap_evn.append(np.sqrt(k0 ** 2 - k_evn[i] ** 2))

	for i in range(0, len(k_odd)): cap_odd.append(np.sqrt(k0 ** 2 - k_odd[i] ** 2))
def calcAB():
	
	for i in range(0, len(cap_evn)): A.append(np.sqrt(1 / (a + 1 / cap_evn[i])))

	for i in range(0, len(cap_odd)): B.append(np.sqrt(1 / (a + 1 / cap_odd[i])))
def genUevn():

	x1 = [i * eps2 for i in range(0, int(a / eps2))]

	x2 = [-i for i in x1[::-1]]

	x3 = [i + a for i in x1]

	x4 = [-i for i in x3[::-1]]
	
	for j in range(0, len(A)):

		y1 = [A[j] * np.cos(k_evn[j] * i) for i in x1]

		y2 = y1[::-1]

		y3 = [A[j] * np.cos(k_evn[j] * i) * np.exp(cap_evn[j] * (a - i)) for i in x3]

		y4 = y3[::-1]

		y_evn.append(y4 + y2 + y1 + y3)


	x_evn.append(x4 + x2 + x1 + x3)
def genUodd():
	
	x1 = [i * eps2 for i in range(0, int(a / eps2))]

	x2 = [-i for i in x1[::-1]]

	x3 = [i + a for i in x1]

	x4 = [-i for i in x3[::-1]]
	
	for j in range(0, len(B)):

		y1 = [B[j] * np.sin(k_odd[j] * i) for i in x1]

		y2 = [-i for i in y1[::-1]]

		y3 = [B[j] * np.sin(k_odd[j] * i) * np.exp(cap_odd[j] * (a - i)) for i in x3]

		y4 = [-i for i in y3[::-1]]

		y_odd.append(y4 + y2 + y1 + y3)

	x_odd.append(x4 + x2 + x1 + x3)


sign                 = -1
k_evn               = sol()
sign                 = 1
k_odd             = sol()
evn_len, odd_len = len(k_evn), len(k_odd)

cap_calc()
calcAB()
genUevn()
genUodd()

f ,(ax1, ax2) = plt.subplots(1, 2)

print("Even: ", evn_len)
print(cap_evn)

print("Odd: ", odd_len)
print(cap_odd)

ax1.plot(x_evn[0], y_evn[0])
ax1.grid(True)
ax1.set_title('Even')

ax2.plot(x_odd[0], y_odd[0])
ax2.grid(True)
ax2.set_title('Odd')



plt.show()
