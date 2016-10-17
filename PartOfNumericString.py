def Un(x, t):

	ser = [(A(i) * np.cos(pl * i * a * t) + B(i) * np.sin(pl * i * a * t)) * np.sin(pl * i * x) for i in range(1, N)]

	return sum(ser)

def UStep(Uij__1, Ui_1j__1, Ui__1j__1, Uij__2):

	#r = a * h_t / h_x

	r = 0.9

	return 2 * (1 - r ** 2) * Uij__1 + (Ui_1j__1 + Ui__1j__1) * (r ** 2) - Uij__2


#Вычислим таблицу
x = np.arange(0, l + h_x, h_x)

UTable = [[],[]]

UTable[0] = [0 if i == 0 or i == len(x) - 1 else InitPos(x[i]) for i in range(len(x))]

UTable[1] = [0 if i == 0 or i == len(x) - 1 else UTable[0][i] + h_t * InitSpeed(x[i]) for i in range(len(x))]

for t in range(2, n_t):

	UTable.append([0])

	for i in range(1, len(x) - 1):

		o = UTable[t - 1][i]
		p = UTable[t - 1][i + 1]
		q = UTable[t - 1][i - 1]
		r = UTable[t - 2][i]

		UTable[-1].append(UStep(o, p, q, r))

	UTable[-1].append(0)

#36:1

def UNum(t_i):

	return UTable[t_i]
