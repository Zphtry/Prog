import math
import matplotlib.pyplot as plt

fact = math.factorial

# начальные значения и переменные
l_left, l_right = .01, 1
delta_l = .05
M, N, m = 10, 10, .9

# 1
X1 = fact(M) / (fact(N) * fact(M - N))
k = 0
X = l_left

P1_k, G1_k, E1_k = [], [], []

while X < l_right:
    X2 = (X / m) ** N
    S, Y = 0, 0
    while Y <= N:
        Y2 = (X / m) ** Y
        Y1 = fact(M) / (fact(Y) * fact(M - Y))
        S += Y1 * Y2
        Y += 1
    P1_k.append(X1 * (X2 / S))
    G1_k.append(X * M * (1 - P1_k[-1]))
    E1_k.append((X * M / m) * (1 - P1_k[-1]))

    XX_k = X
    X += delta_l

# 2
X = l_left
P2_k, G2_k, E2_k = [], [], []

while X < l_right:
    X2 = ((X * M / m) ** N) / fact(N)
    S, Y = 0, 0
    while Y <= (N + 1):
        Y2 = ((X * M / m) ** Y) / fact(Y)
        S += Y2
        Y += 1
    P2_k.append(X2 / S)
    G2_k.append(X * M * (1 - P2_k[-1]))
    E2_k.append((X * M / m) * (1 - P2_k[-1]))
    X += delta_l
    k += 1

# 3
P3_k, G3_k, E3_k = [], [], []

X1 = fact(M) / (fact(N) * fact(M - N))
X = l_left

while X < l_right:
    X2 = (X / (m + X)) ** N
    Y2 = (1 - (X / (m + X))) ** (M - N)
    P3_k.append(X1 * X2 * Y2)
    G3_k.append(X * M * (1 - P3_k[-1]))
    E3_k.append((X * M / m) * (1 - P3_k[-1]))
    X += delta_l

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
