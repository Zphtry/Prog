import numpy as np
import matplotlib.pyplot as plt

from cdf     import CDF
from func    import _func
from fourier import _fourier


N   = 800

T   = 1
Tc  = 1

omc  = 100

t  = np.linspace(0, Tc, N)
om = np.linspace(0, omc, N)

n = 7


func = _func(t, Tc)
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
NN = int(np.fix(Tc / T_disc))
# t1 = np.linspace(0, omc, N)
# t1 = np.arange(0, Tc, T / 900)

# Xn1 = np.zeros(len(t1))
Xn1 = np.zeros(N)

for i in range(N):
  for nn in range(NN + 1):
    Xn1[i] += _func(T * (nn - 1), Tc) * CDF(t[i], T, nn - 1)

# for i in range(len(t1)):
#   for nn in range(NN + 1):
#     Xn1[i] += _func(T * (nn - 1), Tc) * CDF(t1[i], T, nn - 1)

plt.plot(t, Xn1)
plt.show()

# plot(t1,x1);
# plot(t1,Xn1);

# err = abs(x1 - Xn1);
# MaxEps = max(err);
# disp(MaxEps);

# plot(t1,err);
