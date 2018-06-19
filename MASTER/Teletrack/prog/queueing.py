import matplotlib.pyplot as plt
import scipy.misc
import math
from mode_of_work import Mode
fact = math.factorial
comb = scipy.misc.comb


class Queueing:
    def __init__(self, lam, mu, M, N, _range, mode):
        self.lam, self.mu = lam, mu
        self.rho = lam / mu
        self.M, self.N = M, N
        self._range = _range
        self.mode = mode

    """Stage 1"""
    def p_engset(self):
        """engset loss probability / потери по времени"""
        _sum = sum((comb(self.M, n) * (self.rho ** n) for n in range(self.N + 1)))
        return comb(self.M, self.N) * ((self.rho ** self.N) / _sum)

    def p_erlang(self):
        """erlang loss probability / потери по вызовам"""
        _sum = sum(((self.M * self.rho) ** n) / fact(n) for n in range(self.N + 2))
        return (self.M * self.rho) ** self.N / (fact(self.N) * _sum)

    def p_binom(self):
        """binom loss probability"""
        alpha = self.rho / (1 + self.rho)
        return comb(self.M, self.N) * (alpha ** self.N) * (1 - alpha) ** (self.M - self.N)

    """Stage 2"""
    def perf(self, p):
        """performance"""
        return self.lam * self.M * (1 - p)

    """Stage 3"""
    def cons(self, p):
        """connections"""
        return self.rho * self.M * (1 - p)

    def common_plot(self, **kwargs):
        title = f"{kwargs['title']} "
        file_title = f"{kwargs['title_eng']}_"

        if self.mode == Mode.on_lambda:
            variables = f'M={self.M} N={self.N} μ={self.mu}'
            plt.xlabel('λ')
        elif self.mode == Mode.on_mu:
            variables = f'M={self.M} N={self.N} λ={self.lam}'
            plt.xlabel('μ')
        elif self.mode == Mode.on_rho:
            variables = f'M={self.M} N={self.N} λ={self.lam}'
            plt.xlabel('ρ')
        elif self.mode == Mode.on_k:
            variables = f'M={self.M} λ={self.lam} μ={self.mu}'
            plt.xlabel('N')

        title += variables
        file_title += variables.replace(' ', '_').replace('=', '').replace('.', '')
        print(file_title)

        plt.title(title)
        plt.plot(self._range, kwargs['engset'], label='Энгсет')
        plt.plot(self._range, kwargs['erlang'], label='Эрланг')
        plt.plot(self._range, kwargs['binom'], label='Биноминальное распределение')
        plt.legend()
        plt.savefig(file_title.replace('.', '') + '.png')
        plt.show()

