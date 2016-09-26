import matplotlib.pyplot as plt
import numpy as np

om = 1
k = 1

def f1(y, z):

    return z

def f2(y, z):

    return -om * np.sin(y) - k*z


def step(ang_prev, ang_vel_prev):
  
    k1 = h * f1(ang_prev, ang_vel_prev)
    l1 = h * f2(ang_prev, ang_vel_prev)
    
    k2 = h * f1(ang_prev + k1 / 2, ang_vel_prev + l1 / 2)
    l2 = h * f2(ang_prev + k1 / 2, ang_vel_prev + l1 / 2)

    k3 = h * f1(ang_prev + k2 / 2, ang_vel_prev + l2 / 2)
    l3 = h * f2(ang_prev + k2 / 2, ang_vel_prev + l2 / 2)

    k4 = h * f1(ang_prev + k3, ang_vel_prev + l3)
    l4 = h * f2(ang_prev + k3, ang_vel_prev + l3)

    ang = ang_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    ang_vel = ang_vel_prev + (l1 + 2 * l2 + 2 * l3 + l4) / 6

    return ang, ang_vel 


ang0 = 0
ang_vel0 = 8

h = 0.1

X = [ang0]
Y = [ang_vel0]

for i in range(1, 200):
    
    x, y = step(X[-1], Y[-1])

    X.append(x)
    Y.append(y)

plt.plot(X, Y)
plt.grid(True)
plt.show()



