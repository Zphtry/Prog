import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np
import random as rnd
from matplotlib.collections import PatchCollection

L = 100
p = .595

fig, ax = plt.subplots()

forcalc, fordraw = [], []
for i in range(L):
	for j in range(L):
		if rnd.random() <= p:
			forcalc.append([i, j, None])
			fordraw.append(ptch.Rectangle([i, j], 1, 1))

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

n = 7
clrs, clr = np.linspace(0, 1, n), []
for x in forcalc:
	clr.append(clrs[x[2] % n])
coll = PatchCollection(fordraw)
coll.set_array(np.array(clr))
ax.add_collection(coll)


plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.axis('equal')
plt.grid(True)
plt.show()



