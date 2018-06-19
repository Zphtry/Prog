import math
import numpy as np
from queueing import Queueing
from mode_of_work import Mode

fact = math.factorial

"""Режим работы (какой параметр будет меняться)"""
mode = Mode.on_lambda

# поступление нагрузки / уход нагрузки
lam, mu = .9, .9

# число входов / число выходов
M, N = 10, 10

# один из четырёх параметров, который будет меняться
_range = np.arange(.01, 1, .05)


if mode == Mode.on_k:
    _range = np.arange(1, 20)

queueing = Queueing(lam, mu, M, N, _range, mode)

# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []
P2_k, G2_k, E2_k = [], [], []
P3_k, G3_k, E3_k = [], [], []

for var in _range:

    if mode == Mode.on_lambda:
        queueing.lam, queueing.rho = var, var / mu
    elif mode == Mode.on_mu:
        queueing.rho = lam / var
    elif mode == Mode.on_rho:
        queueing.rho = var
    elif mode == Mode.on_k:
        queueing.N = var

    P1_k.append(queueing.p_engset())
    G1_k.append(queueing.perf(P1_k[-1]))
    E1_k.append(queueing.cons(P1_k[-1]))

    P2_k.append(queueing.p_erlang())
    G2_k.append(queueing.perf(P2_k[-1]))
    E2_k.append(queueing.cons(P2_k[-1]))

    P3_k.append(queueing.p_binom())
    G3_k.append(queueing.perf(P3_k[-1]))
    E3_k.append(queueing.cons(P3_k[-1]))

queueing.common_plot(
    title='Вероятность потерь вызовов', title_eng='loss_prob',
    engset=P1_k, erlang=P2_k, binom=P3_k)
queueing.common_plot(
    title='Производительность', title_eng='perf',
    engset=G1_k, erlang=G2_k, binom=G3_k)
queueing.common_plot(
    title='Среднее число соединений', title_eng='aver_conn',
    engset=E1_k, erlang=E2_k, binom=E3_k)
