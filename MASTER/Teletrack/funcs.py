import matplotlib.pyplot as plt
import scipy.misc as scipy_misc
import math
fact = math.factorial


class MassService:
    def __init__(self, lam, mu, M, N, _range, mode):
        self.lam = lam
        self.mu = mu
        self.M = M
        self.N = N
        self._range = _range
        self.rho = lam / mu
        self.comb = scipy_misc.comb(M, N)
        self.mode = mode

    def p_engset(self):
        """engset loss probability"""
        _sum = sum((scipy_misc.comb(self.M, n) * ((self.lam / self.mu) ** n) for n in range(self.N + 1)))
        return self.comb * (((self.lam / self.mu) ** self.N) / _sum)

    def p_erlang(self):
        """erlang loss probability"""
        _sum = sum(((self.M * self.lam / self.mu) ** n) / fact(n) for n in range(self.N + 2))
        return (self.M * self.lam / self.mu) ** self.N / (fact(self.N) * _sum)

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
        title = f"{kwargs['title']}M={self.M}, N={self.N}, mu={self.mu}"
        file_title = (kwargs['title_eng'] + '_M{}_N{}_mu{}').format(self.M, self.N, self.mu)
        plt.title(title)
        plt.plot(self._range, kwargs['engset'], label='Энгсет')
        plt.plot(self._range, kwargs['erlang'], label='Эрланг')
        plt.plot(self._range, kwargs['binom'], label='Биноминальное распределение')
        plt.legend()
        # plt.savefig(file_title.replace('.', '') + '.png')
        plt.show()

