import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np
import random as rnd
from matplotlib.collections import PatchCollection

L = 100
p = .599

fig, ax = plt.subplots()

forcalc, fordraw = [], []
for i in range(L):
	for j in range(L):
		if rnd.random() <= p:
			forcalc.append([i, j, None])
			fordraw.append(ptch.Rectangle((i, j), 1, 1))

def gt(x):
	if x + [None] in forcalc: return True, forcalc.index(x + [None])
	else: return False, 0

n = 0
def dive(x):
	chk = gt(x)
	if chk[0]:
		forcalc[chk[1]][2] = n
		dive([x[0] + 1, x[1],   ])
		dive([x[0] - 1, x[1],   ])
		dive([x[0],     x[1] + 1])
		dive([x[0],     x[1] - 1])
		return True
for x in forcalc:

	if dive(x[:2]): n += 1

clrs = ("orange", "yellow", "green", "lightblue", "blue", "violet")
for i in range(len(forcalc)): fordraw[i].set_fc(clrs[forcalc[i][2] % len(clrs)])
for x in fordraw: ax.add_patch(x)
ax.add_collection(fordraw)

plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.axis('equal')
plt.grid(True)
plt.show()



