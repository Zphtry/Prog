"""
Вероятность потерь вызовов, производительность, среднее число соединений
от интенсивности нагрузки
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as scipy_misc

fact = math.factorial

# интенсивность нагрузки
# начальное значение, шаг, конечное значение
l_left, l_step, l_right = .01, .05, 1

# число входов / число выходов / интенсивность ухода нагрузки
M, N, mu = 10, 10, .9

comb = scipy_misc.comb(M, N)

# параметры коммутатора
# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []
P2_k, G2_k, E2_k = [], [], []
P3_k, G3_k, E3_k = [], [], []


def perf(lam, p):
    """performance"""
    return lam * M * (1 - p)


def cons(_l_to_mu, p):
    """connections"""
    return _l_to_mu * M * (1 - p)


for l in np.arange(l_left, l_right, l_step):
    l_to_mu = l / mu

    part_sum = sum((scipy_misc.comb(M, n) * (l_to_mu ** n) for n in range(N + 1)))
    P1_k.append(comb * (l_to_mu ** N / part_sum))
    G1_k.append(perf(l, P1_k[-1]))
    E1_k.append(cons(l_to_mu, P1_k[-1]))

    part_sum = sum(((M * l_to_mu) ** n) / fact(n) for n in range(N))
    P2_k.append(((M * l_to_mu) ** N) / fact(N) / part_sum)
    G2_k.append(perf(l, P2_k[-1]))
    E2_k.append(cons(l_to_mu, P2_k[-1]))

    alpha = l / (mu + l)
    P3_k.append(comb * (alpha ** N) * (1 - alpha) ** (M - N))
    G3_k.append(perf(l, P3_k[-1]))
    E3_k.append(cons(l_to_mu, P3_k[-1]))

# ylabel('Вероятность потерь вызовов');
# xlabel('Lambda');
# legend('Эрланг', 'Энгсет', 'Биноминальное распределение')
plt.plot(P1_k)
plt.plot(P2_k)
plt.plot(P3_k)
plt.show()

# ylabel('Производительность');
# xlabel('Lambda');
# legend('Эрланг', 'Энгсет', 'Биноминальное распределение')
plt.plot(G1_k)
plt.plot(G2_k)
plt.plot(G3_k)
plt.show()

# ylabel('Среднее число соединений');
# xlabel('Lambda');
# legend('Эрланг', 'Энгсет', 'Биноминальное распределение')
plt.plot(E1_k)
plt.plot(E2_k)
plt.plot(E3_k)
plt.show()
