"""
Вероятность потерь вызовов, производительность, среднее число соединений
от интенсивности нагрузки
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as scipy_misc

fact = math.factorial

# поступление нагрузки
# начальное значение, шаг, конечное значение
l_range = np.arange(.01, 1, .05)

# уход нагрузки
mu = .9

# число входов / число выходов / интенсивность ухода нагрузки
M, N = 20, 10

comb = scipy_misc.comb(M, N)

# параметры коммутатора
# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []
P2_k, G2_k, E2_k = [], [], []
P3_k, G3_k, E3_k = [], [], []


def p_engset(lam):
    _sum = sum((scipy_misc.comb(M, n) * ((lam / mu) ** n) for n in range(N + 1)))
    return comb * (((lam / mu) ** N) / _sum)


def p_erlang(lam):
    _sum = sum(((M * lam / mu) ** n) / fact(n) for n in range(N + 2))
    return (M * lam / mu) ** N / fact(N) / _sum


def p_binom(lam):
    alpha = lam / (mu + lam)
    return comb * (alpha ** N) * (1 - alpha) ** (M - N)


def perf(lam, p):
    """performance"""
    return lam * M * (1 - p)


def cons(lam, p):
    """connections"""
    return perf(lam, p) / mu


def common_plot(**kwargs):
    plt.title((kwargs['title'] + ' M={}, N={}, mu={}').format(M, N, mu))
    plt.plot(l_range, kwargs['engset'], label='Энгсет')
    plt.plot(l_range, kwargs['erlang'], label='Эрланг')
    plt.plot(l_range, kwargs['binom'], label='Биноминальное распределение')
    plt.legend()
    plt.show()


for l in l_range:
    P1_k.append(p_engset(l))
    G1_k.append(perf(l, P1_k[-1]))
    E1_k.append(cons(l, P1_k[-1]))

    P2_k.append(p_erlang(l))
    G2_k.append(perf(l, P2_k[-1]))
    E2_k.append(cons(l, P2_k[-1]))

    P3_k.append(p_binom(l))
    G3_k.append(perf(l, P3_k[-1]))
    E3_k.append(cons(l, P3_k[-1]))

common_plot(title='Вероятность потерь вызовов', engset=P1_k, erlang=P2_k, binom=P3_k)
common_plot(title='Производительность',         engset=G1_k, erlang=G2_k, binom=G3_k)
common_plot(title='Среднее число соединений',   engset=E1_k, erlang=E2_k, binom=E3_k)
