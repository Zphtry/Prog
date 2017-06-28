import numpy as np
#очень трудно запомнить, но попробуй
#[НОМЕР СТРОКИ][НОМЕР СТОЛБЦА]

#<nord-west>
#row or column make zero exept 
def row_mkz(ic, jc):

	for i in range(n_cols):
		
		if i != jc and sols[ic][i] == 0: sols[ic][i] = '-'

def col_mkz(ic, jc):

	for i in range(n_rows):
		
		if i != ic and sols[i][jc] == 0: sols[i][jc] = '-'

def diag_mod(ib, jb, dlen):

	for s in range(dlen):

		if sols[ib + s][jb - s] == '-': continue

		val = min(supl[ib + s], cust[jb - s])

		sols[ib + s][jb - s] = val

		supl[ib + s] -= val

		cust[jb - s] -= val

		if supl[ib + s] == 0: row_mkz(ib + s, jb - s)

		elif cust[jb - s] == 0: col_mkz(ib + s, jb - s)


prce = [
[3, 1, 2, 2, 4],
[1, 5, 4, 9, 3],
[5, 4, 7, 3, 2]]

#поставщик
supl = [50, 80, 60]

#клиент
cust = [20, 35, 25, 70, 40]


n_rows, n_cols = len(supl), len(cust)

sols = [[0] * n_cols for i in range(n_rows)]

#проход до побочной диагонали включительно
for d in range(n_cols):

	diag_mod(0, d, min(d + 1, n_rows))

#проход после побочной диагонали
for d in range(1, n_rows):

	diag_mod(d, -1, min(n_rows - d, n_cols))


print(sols)
#</nord-west>
#until all evals are negative

def gd_prnt(lst):

	for i in lst: print(i['stat'], i['i'], i['j'],'(' + str(sols[i['i']][i['j']]) + ')')

	up, dwn, rght, lft = '↑', '↓', '→', '←'

	net = [[0] * n_cols for i in range(n_rows)]

	for i in range(len(lst)):

		ti, tj = lst[i]['i'], lst[i]['j']

		net[ti][tj] = '★p+' if i == 0 else lst[i]['stat']

		di, dj = lst[(i + 1) % len(lst)]['i'] - ti, lst[(i + 1) % len(lst)]['j'] - tj

		if abs(di) > 1:

			for k in range(ti + np.sign(di), ti + di, np.sign(di)):

				net[k][tj] = dwn if di > 0 else up

		if abs(dj) > 1:

			for k in range(tj + np.sign(dj), tj + dj, np.sign(dj)):

				net[ti][k] = rght if dj > 0 else lft


	for k in net: print(k)

	print('\n')  

def mk_sqnce(hst, i, j):

	beg = hst[-1]

	if(j == '-'):

		lsg = np.sign(i - beg['i'])

		mid = [{'i': k, 'j': beg['j'], 'stat': 'n'} for k in range(beg['i'] + lsg, i, lsg)]

		end = {'i': i, 'j': beg['j']}

	if(i == '-'):

		lsg = np.sign(j - beg['j'])

		mid = [{'i': beg['i'], 'j': k, 'stat': 'n'} for k in range(beg['j'] + lsg, j, lsg)]

		end = {'i': beg['i'], 'j': j}

	if beg['stat'] == 'p+': end['stat'] = 'p-'
	elif beg['stat'] == 'p-': end['stat'] = 'p+'

	return mid + [end]

def is_ij_in_sq(i, j, sq):

	log = False

	for k in ['n', 'p+', 'p-']: log = log or {'i': i, 'j': j, 'stat': k} in sq

	return log

def iter(hst):

	beg = hst[0]

	end = hst[-1]

	if len(hst) > 1 and beg['i'] == end['i'] and beg['j'] == end['j']:

		prbl_sols.append(hst)

		return

	for i in range(n_rows):

		is_strt = i == beg['i'] and end['j'] == beg['j']

		do_exst = sols[i][end['j']] != '-'

		is_not_curr = i != end['i'] 

		if  is_not_curr and (is_strt or (do_exst and not is_ij_in_sq(i, end['j'], hst))):

			iter(hst + mk_sqnce(hst, i, '-'))


	for j in range(n_cols):

		is_strt = end['i'] == beg['i'] and j == beg['j']

		do_exst = sols[end['i']][j] != '-'

		is_not_curr = j != end['j'] 

		if is_not_curr and (is_strt or (do_exst and not is_ij_in_sq(end['i'], j, hst))):

			iter(hst + mk_sqnce(hst, '-', j))		

for l in range(500):

	#<Нахождение альф и бет>
	#матрица и правая часть
	abma, b = [], []

	#заполнение матрицы
	for i in range(n_rows):

		for j in range(n_cols):

			if sols[i][j] != '-':

				abma.append([0] * (n_rows + n_cols - 1))

				#запись alph 
				if i != 0: abma[-1][i - 1] = 1

				#запись beta
				abma[-1][n_rows + j - 1] = 1

				b.append(prce[i][j])

	ab = [0] + np.linalg.solve(abma, b).tolist()
	#</Нахождение альф и бет>
	print(ab)
	#<Вычисление оценок>
	evls = []

	for i in range(n_rows):

		for j in range(n_cols):

			if sols[i][j] == '-':

				print(i+1,j+1,' ',prce[i][j], ab[i], ab[n_rows + j],' ', prce[i][j] - (ab[i] + ab[n_rows + j]))

				evls.append({'i': i, 'j': j, 'val': prce[i][j] - (ab[i] + ab[n_rows + j])})

	evls.sort(key = lambda x: x['val'])

	if evls[0]['val'] >= 0: break
	#</Вычисление оценок>

	#<Означенный цикл>
	prbl_sols = []

	strt = {'i': evls[0]['i'], 'j': evls[0]['j'], 'stat': 'p+'}

	iter([strt])

	#<Фильтрация>
	prbl_sols = [[y for y in x[:len(x) - 1] if y['stat'] != 'n' ] for x in prbl_sols]

	prbl_sols = [x for x in prbl_sols if len(x) % 2 == 0]

	bst_sols = []

	for x in prbl_sols:
		
		rows = [0] * n_rows

		cols = [0] * n_cols

		for y in x:
			
			rows[y['i']] += 1

			cols[y['j']] += 1

		for c in rows:
			if c % 2 != 0: break

		else:

			for c in cols:

				if c % 2 != 0: break

			else: bst_sols.append(x)
	#</Фильтрация>

	#<Изменение на teta>
	sqnce = bst_sols[0]

	teta = min([sols[x['i']][x['j']] for x in sqnce if x['stat'] == 'p-'])

	gd_prnt(sqnce)

	for x in sqnce:
		
		if sols[x['i']][x['j']] == '-' : sols[x['i']][x['j']] = teta

		elif x['stat'] == 'p+': sols[x['i']][x['j']] += teta

		elif x['stat'] == 'p-':

			sols[x['i']][x['j']] -= teta

			if sols[x['i']][x['j']] == 0: sols[x['i']][x['j']] = '-'
	#</Изменение на teta>

	for k in sols: print(k)

	print('\n')

min_val = 0

for i in range(n_rows):

	for j in range(n_cols):

		if(sols[i][j] != '-'): min_val += sols[i][j] * prce[i][j]

print(min_val)

