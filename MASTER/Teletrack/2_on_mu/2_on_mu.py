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
lam = .9

# уход нагрузки
# начальное значение, шаг, конечное значение
mu_range = np.arange(.01, 1, .05)

# число входов / число выходов
M, N = 50, 10

comb = scipy_misc.comb(M, N)

# параметры коммутатора
# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []
P2_k, G2_k, E2_k = [], [], []
P3_k, G3_k, E3_k = [], [], []


def p_engset(_mu):
    _sum = sum((scipy_misc.comb(M, n) * ((lam / _mu) ** n) for n in range(N + 1)))
    return comb * (((lam / _mu) ** N) / _sum)


def p_erlang(_mu):
    _sum = sum(((M * lam / _mu) ** n) / fact(n) for n in range(N + 2))
    return (M * lam / _mu) ** N / (fact(N) * _sum)


def p_binom(_mu):
    alpha = lam / (_mu + lam)
    return comb * (alpha ** N) * (1 - alpha) ** (M - N)


def perf(p):
    """performance"""
    return lam * M * (1 - p)


def cons(_mu, p):
    """connections"""
    return perf(p) / _mu


def common_plot(**kwargs):
    title = (kwargs['title'] + ' M={}, N={}, lam={}').format(M, N, lam)
    file_title = (kwargs['title_eng'] + '_M{}_N{}_lam{}').format(M, N, lam)
    plt.title(title)
    plt.plot(mu_range, kwargs['engset'], label='Энгсет')
    plt.plot(mu_range, kwargs['erlang'], label='Эрланг')
    plt.plot(mu_range, kwargs['binom'], label='Биноминальное распределение')
    plt.legend()
    plt.savefig(file_title.replace('.', '') + '.png')
    plt.show()


for _mu in mu_range:
    P1_k.append(p_engset(_mu))
    G1_k.append(perf(P1_k[-1]))
    E1_k.append(cons(_mu, P1_k[-1]))

    P2_k.append(p_erlang(_mu))
    G2_k.append(perf(P2_k[-1]))
    E2_k.append(cons(_mu, P2_k[-1]))

    P3_k.append(p_binom(_mu))
    G3_k.append(perf(P3_k[-1]))
    E3_k.append(cons(_mu, P3_k[-1]))

common_plot(title='Вероятность потерь вызовов', title_eng='loss_prob', engset=P1_k, erlang=P2_k, binom=P3_k)
common_plot(title='Производительность', title_eng='perf', engset=G1_k, erlang=G2_k, binom=G3_k)
common_plot(title='Среднее число соединений', title_eng='aver_conn', engset=E1_k, erlang=E2_k, binom=E3_k)
