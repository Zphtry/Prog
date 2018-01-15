import numpy as np
import matplotlib.pyplot as plt




def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 3.0, 0.01)

ax1 = plt.subplot(311)
ax1.plot(t1, f(t1), 'k')



ax2 = plt.subplot(323)
ax2.plot(t1, f(t1), 'r')

ax2 = plt.subplot(324)
ax2.plot(t1, f(t1), 'b')

ax3 = plt.subplot(313)
ax3.plot(t1, f(t1), 'g')

# 222
# 221
# 212



plt.show()

exit()

'''Цель работы'''
# Выполнить над сигналом преобразование Фурье
# Построить амплитудную и частотную характеристику сигнала
# Восстановить исходный сигнал
A, tau = 2, .5

def _func(arg):

  return A * np.exp(-arg / tau) if 0 <= arg.all() < t[-1] else 0

# def fourier(arg):


N  = 100
t  =  np.linspace(0, .8, N)

func = _func(t)


# fourier transform
fou = []
W  = np.linspace(0, 3000, N, endpoint=False)
for i in range(N):
  re = np.trapz(np.multiply(func, np.cos(t * W[i])))
  im = np.trapz(np.sin(t * W[i]), x=t)
  fou.append(re + im * 1j)

# амплитуды
amp = list(map(lambda arg: np.abs(arg), fou))

# частоты
frq  = list(map(lambda arg: np.angle(arg), fou))

# восстановленная функция
rst  = []
for i in range(N):
  rst.append((1 / (2 * np.pi)) * np.trapz(np.multiply(fou, np.exp(np.multiply(W, t[i] * 1j))), x=W))


f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')

# plt.plot(W, rst)
# plt.show()