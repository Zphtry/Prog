import matplotlib.pyplot as plt
import numpy as np

h = 0.01

t_r = 25

vic0, pred0 = 3, 4

#1/sec 1/(sec*pred)
a1, b1 = .9, .1

#1/sec 1/(sec*vic)
a2, b2 = .4, .5

def dvic(x, y):

	return x * (a1 - b1 * y)

def dpred(x, y):

	return y * (-a2 + b2 * x)

def step(vic_prev, pred_prev):
  
    k1 = h * dvic(vic_prev, pred_prev)
    l1 = h * dpred(vic_prev, pred_prev)
    
    k2 = h * dvic(vic_prev + k1 / 2, pred_prev + l1 / 2)
    l2 = h * dpred(vic_prev + k1 / 2, pred_prev + l1 / 2)

    k3 = h * dvic(vic_prev + k2 / 2, pred_prev + l2 / 2)
    l3 = h * dpred(vic_prev + k2 / 2, pred_prev + l2 / 2)

    k4 = h * dvic(vic_prev + k3, pred_prev + l3)
    l4 = h * dpred(vic_prev + k3, pred_prev + l3)

    vic = vic_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    pred = pred_prev + (l1 + 2 * l2 + 2 * l3 + l4) / 6

    return vic, pred



T = [0]
Vic = [vic0]
Pred = [pred0]

for i in range(1, int(t_r/h)):
    
    x, y = step(Vic[-1], Pred[-1])

    T.append(i * h)
    Vic.append(x)
    Pred.append(y)

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(Vic, Pred)
ax1.set_title("Phase")
ax2.plot(T, Pred)
ax2.plot(T, Vic, 'r')
ax2.set_title("Red - victim")

plt.show()