import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

N = 20

a = 2

l = 3

pl = np.pi / l

h = 0.01


def InitPos(x):

	if x == 0 or x == l: return 0

	return np.exp(- (x - 2) ** 2)

def InitSpeed(x):
	return 0

def AFunc(x, n):

	return InitPos(x) * np.sin(pl * n * x)

def BFunc(x, n):

	return InitSpeed(x) * np.sin(pl * n * x)

def AInteger(n):

	sum41 = 0

	for i in range(int(l / h)): sum41 += AFunc(i * h, n) * h

	return sum41

def BInteger(n):

	sum41 = 0

	for i in range(int(l / h)): sum41 += BFunc(i * h, n) * h

	return sum41

def A(n):

	return AInteger(n) * 2 / l

def B(n):

	return (BInteger(n) * 2) / (np.pi * n * a)

def U(x, t):

	ser = [(A(i) * np.cos(pl * i * a * t) + B(i) * np.sin(pl * i * a * t)) * np.sin(pl * i * x) for i in range(1, N)]

	return sum(ser)

#Всё, что ниже, отвечает за построение
fig, ax = plt.subplots()

X = np.arange(0.0, l, h)
line, = ax.plot(X, U(X, 0))

def animate(i):
    line.set_ydata(U(X, i/50))  # update the data
    return line,

def init():
    line.set_ydata(np.ma.array(X, mask=True))
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, 2000), init_func=init, interval=1, blit=True)
ax.set_ylim([-1,1])
plt.show()
