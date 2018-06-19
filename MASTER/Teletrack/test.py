import math
fact = math.factorial
from funcs import MassService
from mode_of_work import Mode
import numpy as np
import scipy.misc as scipy_misc


"""Режим работы (какой параметр будет меняться)"""
mode = Mode.on_lambda

# поступление нагрузки / уход нагрузки / соотношение
lam, mu = 0, .9; rho = lam / mu

# число входов / число выходов
M, N = 50, 10

# один из четырёх параметров, который будет меняться
_range = np.arange(.01, 1, .05)

comb = scipy_misc.comb(M, N)

# вероятность потерь вызовов / производительность / среднее число соединений
P1_k, G1_k, E1_k = [], [], []
P2_k, G2_k, E2_k = [], [], []
P3_k, G3_k, E3_k = [], [], []

# if mode == Mode.on_lambda:
#     pass
# elif mode == Mode.on_mu:
#     pass
# elif mode == Mode.on_rho:
#     pass
# elif mode == Mode.on_k:
#     pass

mass_service = MassService(lam, mu, M, N, _range, mode)

for var in _range:

    if mode == Mode.on_lambda:
        mass_service.lam = var
    elif mode == Mode.on_mu:
        pass
    elif mode == Mode.on_rho:
        pass
    elif mode == Mode.on_k:
        pass

    P1_k.append(mass_service.p_engset())
    G1_k.append(mass_service.perf(P1_k[-1]))
    E1_k.append(mass_service.cons(P1_k[-1]))

    P2_k.append(mass_service.p_erlang())
    G2_k.append(mass_service.perf(P2_k[-1]))
    E2_k.append(mass_service.cons(P2_k[-1]))

    P3_k.append(mass_service.p_binom())
    G3_k.append(mass_service.perf(P3_k[-1]))
    E3_k.append(mass_service.cons(P3_k[-1]))

common_plot(title='Вероятность потерь вызовов', title_eng='loss_prob', engset=P1_k, erlang=P2_k, binom=P3_k)
common_plot(title='Производительность', title_eng='perf', engset=G1_k, erlang=G2_k, binom=G3_k)
common_plot(title='Среднее число соединений', title_eng='aver_conn', engset=E1_k, erlang=E2_k, binom=E3_k)