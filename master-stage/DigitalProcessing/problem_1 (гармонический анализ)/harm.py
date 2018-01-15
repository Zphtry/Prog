import numpy as np
import matplotlib.pyplot as plt

'''Цель работы'''
# Выполнить над сигналом преобразование Фурье
# Построить амплитудную и частотную характеристику сигнала
# Восстановить исходный сигнал

N  = 100

t  =  np.linspace(0, .8, N)

W  = np.linspace(0, 3000, N, endpoint=False)

func = np.zeros(N)

A, tau = 2, .5
for i in range(N):
  func[i] = A * np.exp(-t[i] / tau) if 0 <= t[i] < t[-1] else 0

# fourier transform
fou = []
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

plt.plot(W, rst)
plt.show()