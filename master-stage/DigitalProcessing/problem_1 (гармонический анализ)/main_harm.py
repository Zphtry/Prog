import numpy as np
import matplotlib.pyplot as plt

'''Цель работы'''
# Выполнить преобразование Фурье над сигналом
# Построить амплитудную и частотную характеристику сигнала
# Восстановить исходный сигнал

A, tau = 2, .5
def _func(arg):

  return A * np.exp(-arg / tau) if 0 <= arg.all() < t[-1] else 0

N  = 300
t  =  np.linspace(0, .7, N)

func = _func(t)

ax1 = plt.subplot(221)
ax1.plot(t, func, 'r')
ax1.set_title('Original')

# преобразование Фурье
fou = []
om  = np.linspace(0, 2000, N)
for i in range(N):
  re = np.trapz(func * np.cos(t * om[i]), x=t)
  im = np.trapz(func * np.sin(t * om[i]), x=t)
  fou.append(re - im * 1j)

# амплитуды
ax2 = plt.subplot(223)
ax2.plot(om, np.abs(fou))
ax2.set_title('Amplitudes')

# частоты
ax3 = plt.subplot(224)
ax3.plot(om, np.angle(fou))
ax3.set_title('Frequencies')

# восстановленная функция
rst  = []
for i in range(N):
  a = np.trapz(np.real(fou) * np.cos(om * t[i]), x = om)
  b = np.trapz(np.imag(fou) * np.sin(om * t[i]), x = om)
  rst.append((a - b) / np.pi)

ax4 = plt.subplot(222)
ax4.plot(t, rst, 'g')
ax4.set_title('Restored')

# plt.plot(t, rst, 'g')
# plt.title('Restored')
# plt.savefig('restored.png')
# exit()

plt.tight_layout()
plt.show()