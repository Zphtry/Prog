import matplotlib.pyplot as plt
import numpy as np


t_end = 200

h = 0.01


x0, y0 = 100, 56

r, K, W, D = 1, 1.5, 1, 1

S, J = .2, .5


def dx(x, y):

	return r * (1 - x / K) * x - x * y * W / (D + x) 

def dy(x, y):

	return S * y * (1 - J * y / x)


def step(x_prev, y_prev):
  
    k1 = h * dx(x_prev, y_prev)
    l1 = h * dy(x_prev, y_prev)
    
    k2 = h * dx(x_prev + k1 / 2, y_prev + l1 / 2)
    l2 = h * dy(x_prev + k1 / 2, y_prev + l1 / 2)

    k3 = h * dx(x_prev + k2 / 2, y_prev + l2 / 2)
    l3 = h * dy(x_prev + k2 / 2, y_prev + l2 / 2)

    k4 = h * dx(x_prev + k3, y_prev + l3)
    l4 = h * dy(x_prev + k3, y_prev + l3)

    x_ret = x_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    y_ret = y_prev + (l1 + 2 * l2 + 2 * l3 + l4) / 6

    return x_ret, y_ret




T = [0]
X = [x0]
Y = [y0]

for i in range(1, int(t_end/h)):
    
    x, y = step(X[-1], Y[-1])

    T.append(i * h)
    X.append(x)
    Y.append(y)

f, (ax1, ax2) = plt.subplots(1, 2)

a, bet = D / K, S/ r

cond1 = a >= 1 or a < 1 and a + bet >= 1

cond2 = a + bet < 1 and (1 - a - bet) ** 2 - 8 * a * bet <=0

print(a, bet)

print(cond1, cond2)

ax1.plot(X, Y)
ax1.set_title("Phase")
ax2.plot(T, Y)
ax2.plot(T, X, 'r')
ax2.set_title("Red - victim")

plt.show()