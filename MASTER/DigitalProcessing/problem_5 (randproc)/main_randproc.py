import numpy as np
import matplotlib.pyplot as plt

from rp import RP
from funcs import R

N, a, b = 500, .24, 2

x = RP(N, a, b)

plt.hist(x, int(np.sqrt(N)))
plt.title('Гистограмма распределения случайной величины')
plt.savefig('hist.png')
plt.show()

#  математическое ожидание
m = np.mean(x)
print('Математическое ожидание',m)

# дисперсия (квадрат среднекватратичного отклонения)
d = np.mean((x - m) ** 2)
print('Дисперсия', d)

r = R(x, m)

plt.plot(np.arange(-N // 10 + 1, N // 10 - 1), r)
plt.title('Оценка корелляционной функции')
plt.savefig('corell.png')
plt.show()
