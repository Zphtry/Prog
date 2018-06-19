import matplotlib.pyplot as plt
import scipy.misc as scipy_misc
import math
from mode_of_work import Mode
fact = math.factorial


class Queueing:
    def __init__(self, lam, mu, M, N, _range, mode):
        self.lam, self.mu = lam, mu
        self.M, self.N = M, N
        self._range = _range
        self.rho = lam / mu
        self.comb = scipy_misc.comb(M, N)
        self.mode = mode

    def p_engset(self):
        """engset loss probability"""
        _sum = sum((scipy_misc.comb(self.M, n) * (self.rho ** n) for n in range(self.N + 1)))
        return self.comb * ((self.rho ** self.N) / _sum)

    def p_erlang(self):
        """erlang loss probability"""
        _sum = sum(((self.M * self.rho) ** n) / fact(n) for n in range(self.N + 2))
        return (self.M * self.rho) ** self.N / (fact(self.N) * _sum)

    def p_binom(self):
        """binom loss probability"""
        alpha = self.rho / (1 + self.rho)
        return self.comb * (alpha ** self.N) * (1 - alpha) ** (self.M - self.N)

    def perf(self, p):
        """performance"""
        return self.lam * self.M * (1 - p)

    def cons(self, p):
        """connections"""
        return self.perf(p) / self.mu

    def common_plot(self, **kwargs):
        title = f"{kwargs['title']} "
        if self.mode == Mode.on_lambda:
            title += f'M={self.M} N={self.N} μ={self.mu}'
            plt.xlabel('λ')
        elif self.mode == Mode.on_mu:
            title += f'M={self.M} N={self.N} λ={self.lam}'
            plt.xlabel('μ')
        elif self.mode == Mode.on_rho:
            title += f'M={self.M} N={self.N}'
            plt.xlabel('ρ')
        elif self.mode == Mode.on_k:
            title += f'M={self.M} N={self.N} ρ={self.rho}'
            plt.xlabel('k = M / N')

    # file_title = f"_M{self.M}_N{self.N}_mu{self.mu}"

        plt.title(title)
        plt.plot(self._range, kwargs['engset'], label='Энгсет')
        plt.plot(self._range, kwargs['erlang'], label='Эрланг')
        plt.plot(self._range, kwargs['binom'], label='Биноминальное распределение')
        plt.legend()
        # plt.savefig(file_title.replace('.', '') + '.png')
        plt.show()

