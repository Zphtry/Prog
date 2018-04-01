import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np
import random as rnd
from matplotlib.collections import PatchCollection

L = 30
p = .58

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



clsts = []
for x in forcalc:
	if x[2] < len(clsts): clsts[x[2]].append(x[:-1])
	else: clsts.append([x[:-1]])

def sel_min(x, crd):
	x = np.array(x)
	i = x[:, crd].tolist().index(min(x[:, crd]))
	return min(x[:, crd]) == 0, i
def sel_max(x, crd):
	x = np.array(x)
	i = x[:, crd].tolist().index(max(x[:, crd]))
	return max(x[:, crd]) == L - 1, i
good_clsts = []
for x in clsts:
	#выборка по x
	if sel_min(x, 0)[0] and sel_max(x, 0)[0]:
		good_clsts.append(x)
		good_clsts[-1].append('hor')
	elif sel_min(x, 1)[0] and sel_max(x, 1)[0]:
		good_clsts.append(x)
		good_clsts[-1].append('ver')

#make way
#ищем какое-нибудь начало кластера и какой-нибудь конец
beg, end = 0, 0
for x in good_clsts:
	if x[-1] == 'hor':
		beg = x[sel_min(x[:-1], 0)[1]]
		end = x[sel_max(x[:-1], 0)[1]]
		break

	if x[-1] == 'ver':
		beg = x[sel_min(x[:-1], 1)[1]]
		end = x[sel_max(x[:-1], 1)[1]]
		break
if len(good_clsts) > 0: good_clsts = good_clsts[0]
print(beg, end)

seq = []
def dive_seq(x, hst):
	if x not in hst and x in good_clsts and len(seq) == 0:
		if x == end:
			global seq
			seq = list(hst) + [end]
			return
		if good_clsts[-1] == 'ver':
			print(x)
			dive_seq([x[0], x[1] + 1], hst + [x])
			dive_seq([x[0] + 1, x[1]], hst + [x])
			dive_seq([x[0] - 1, x[1]], hst + [x])
			dive_seq([x[0], x[1] - 1], hst + [x])
		if good_clsts[-1] == 'hor':
			print(x)
			dive_seq([x[0] + 1, x[1]], hst + [x])
			dive_seq([x[0], x[1] + 1], hst + [x])
			dive_seq([x[0], x[1] - 1], hst + [x])
			dive_seq([x[0] - 1, x[1]], hst + [x])
		
dive_seq(beg, [])

clrs = ("orange", "yellow", "green", "lightblue", "blue", "violet")
for i in range(len(forcalc)):
	if forcalc[i][:2] in seq:
		fordraw[i].set_fc("red")
		# plt.text(forcalc[i][0] + .5, forcalc[i][1] + .5, str(forcalc[i][0]) +','+ str(forcalc[i][1]), ha="center", family='sans-serif', size=5)
	else: fordraw[i].set_fc(clrs[forcalc[i][2] % len(clrs)])
for x in fordraw: ax.add_patch(x)

plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.axis('equal')
plt.grid(True)
# plt.savefig('a.png', dpi=300)
plt.show()
