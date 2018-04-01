import matplotlib.pyplot as plt
import numpy as np

om = 1
k = 0

t_r = 50

ang0 = 0
ang_vel0 = 4

h = 0.01

def simp_sin(t):

    C1, C2 = ang_vel0, ang0

    return C1 * np.sin(t) + C2 * np.cos(t)

def dsimp_sin(t):
    
    C1, C2 = ang_vel0, ang0

    return C1 * np.cos(t) - C2 * np.sin(t)

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

Ang = [ang0]
Ang_vel = [ang_vel0]
Simp_sin = [ang0]
DSimp_sin = [ang_vel0]

T = [0]

for i in range(1, int(t_r/h)):
    
    x, y = step(Ang[-1], Ang_vel[-1])

    T.append(i * h)
    Ang.append(x)
    Ang_vel.append(y)
    Simp_sin.append(simp_sin(T[-1]))
    DSimp_sin.append(dsimp_sin(T[-1]))

f, axarr = plt.subplots(2, 2)

axarr[0, 0].plot(T, Ang)
axarr[0, 0].set_title('Angle(t)')
axarr[0, 0].plot(T, Simp_sin, 'r')

axarr[0, 1].plot(T, Ang_vel)
axarr[0, 1].set_title('Angular_velocity(t)')
axarr[0, 1].plot(T, DSimp_sin, 'r')

axarr[1, 0].plot(Ang, Ang_vel)
axarr[1, 0].set_title('Angular_velocity(angle)')
axarr[1, 0].plot(Simp_sin, DSimp_sin, 'r')

for x in axarr:
    for y in x:
        y.grid(True)
        
plt.show()

plt.show()
