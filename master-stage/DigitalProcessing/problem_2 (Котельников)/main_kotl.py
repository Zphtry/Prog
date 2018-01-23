import numpy as np
import matplotlib.pyplot as plt

from cdf     import CDF
from func    import _func
from fourier import _fourier

N = 800


#период функции отсчётов
T = .1

T_max  = 1
om_max = 100

t  = np.linspace(0, T_max, N)
om = np.linspace(0, om_max, N)

n = 7

func = np.array(list(map(lambda x: _func(x, T_max), t)))
sp_1 = plt.subplot(221)
sp_1.plot(t, func, color=(0, .9, 0))
sp_1.set_title('Заданный сигнал')

amp_func = np.abs(_fourier(func, t, om))
sp_2 = plt.subplot(223)
sp_2.plot(om, amp_func, color=(0, .5, 0))
sp_2.set_title('Амплитудная характеристика')

count_f = CDF(t, T, n)
sp_3 = plt.subplot(222)
sp_3.plot(t, count_f, color=(0, 0, .9))
sp_3.set_title('Функция отсчётов')

fou = _fourier(count_f, t, om)
sp_4 = plt.subplot(224)
sp_4.plot(t, np.real(fou), color=(0, 0, .5))
sp_4.set_title('Спектральная характеристика')

plt.tight_layout()
plt.show()

max_amp = .05 * max(amp_func)
for i in range(N):
  if amp_func[i] <= max_amp:
    freq = om[i]

print(freq)

T_disc = np.pi / freq
NN = int(np.fix(T_max / T_disc))

func_recovered = np.zeros(N)
for i in range(N):
  for nn in range(NN + 1):
    func_recovered[i] += _func(T * (nn - 1), T_max) * CDF(t[i], T, nn - 1)

plt.plot(t, func)
plt.plot(t, func_recovered)
plt.show()

err = abs(func - func_recovered)
# MaxEps = max(err);
# disp(MaxEps);

plt.plot(t, err)
plt.show()
