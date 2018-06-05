import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as scipy_misc

fact = math.factorial

# интенсивность потока поступления нагрузки
# начальное значение, шаг, конечное значение
l_left, l_step, l_right = .01, .05, 1

# число входов / число выходов / интенсивность ухода нагрузки
M, N, mu = 10, 10, .9

"""
Вероятность потерь вызовов, производительность, среднее число соединений 
от интенсивности нагрузки
"""
comb = scipy_misc.comb(M, N)

# параметры коммутатора
# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []

for l in np.arange(l_left, l_right, l_step):
    l_to_mu_ratio = l / mu
    part_sum = sum((scipy_misc.comb(M, n) * (l_to_mu_ratio ** n) for n in range(N + 1)))

    P1_k.append(comb * (l_to_mu_ratio ** N / part_sum))
    G1_k.append(l * M * (1 - P1_k[-1]))
    E1_k.append((l_to_mu_ratio * M) * (1 - P1_k[-1]))

plt.plot(P1_k)
plt.show()
exit()

# 2
X = l_left
P2_k, G2_k, E2_k = [], [], []

while X < l_right:
    X2 = ((X * M / mu) ** N) / fact(N)
    S, Y = 0, 0
    while Y <= (N + 1):
        Y2 = ((X * M / mu) ** Y) / fact(Y)
        S += Y2
        Y += 1
    P2_k.append(X2 / S)
    G2_k.append(X * M * (1 - P2_k[-1]))
    E2_k.append((X * M / mu) * (1 - P2_k[-1]))
    X += l_step

# 3
P3_k, G3_k, E3_k = [], [], []

X1 = fact(M) / (fact(N) * fact(M - N))
X = l_left

while X < l_right:
    X2 = (X / (mu + X)) ** N
    Y2 = (1 - (X / (mu + X))) ** (M - N)
    P3_k.append(X1 * X2 * Y2)
    G3_k.append(X * M * (1 - P3_k[-1]))
    E3_k.append((X * M / mu) * (1 - P3_k[-1]))
    X += l_step

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
