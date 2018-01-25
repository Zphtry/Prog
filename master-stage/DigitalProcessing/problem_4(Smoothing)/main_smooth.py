import numpy as np
import matplotlib.pyplot as plt

from f import F
from r import R
from ma import MA
from ols import OLS
from mofd import MoFD
from em import EM

N = 200
w = np.arange(0, N)

x = F(N)
r = R(N)
y = x + r

ax1 = plt.subplot(311)
ax1.plot(w, x)
ax1.set_title('Чистый сигнал')

ax2 = plt.subplot(312)
ax2.plot(w, r)
ax2.set_title('Шум')


ax3 = plt.subplot(313)
ax3.plot(w, y)
ax3.set_title('Зашумленный сигнал')

plt.tight_layout()
plt.savefig('initial.png')
plt.show()


'''скользящее среднее'''

L = [2, 4, 6, 8]


MovAve = np.zeros((len(L), N))

for i in range(len(L)):
  MovAve[i, :] = MA(y, L[i])
  sp = plt.subplot(221 + i)
  sp.plot(w, MovAve[i,:])
  sp.set_title('L = ' + str(L[i]))

plt.tight_layout()
plt.savefig('ma.png')
plt.show()



MovAveOLS = np.zeros(len(L))
for n in range(len(L)):
  MovAveOLS[n] = round(OLS(MovAve[n,:], x), 3)

print(MovAveOLS) # среднеквадратичное отклонение



'''четвёртые разности'''
M2 = MoFD(y)
M2OLS = OLS(M2,x)
print(M2OLS)

plt.plot(w, M2)
plt.savefig('fourth_diff.png')
plt.show()

'''экспоненциальное сглаживание'''
a = np.arange(.1, 1, .1)

M3 = np.zeros((len(a), N))
for i in range(len(a)):
  M3[i, :] = EM(y, a[i])
  print(a[i],':',round(OLS(M3[i, :], x)))
  sp = plt.subplot(331 + i)
  sp.plot(w, M3[i,:])
  sp.set_title('a = ' + str(a[i]))

plt.tight_layout()
plt.savefig('exp.png')
plt.show()
exit()

# экспоненциальное сглаживание
M3OLS = np.zeros(len(a))
for n in range(len(a)):
  M3OLS[n] = OLS(M3[n, :], x)

print(M3OLS)

plt.plot(a, M3OLS)
plt.show()
