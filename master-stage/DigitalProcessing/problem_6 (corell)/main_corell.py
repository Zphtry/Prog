import numpy as np
import matplotlib.pyplot as plt

from search import Search

#section 1

N = 2 ** 11
T = 2e-2
t = np.linspace(0, T, N)
# t = t(1:end-1);


A = 2
fi = 2.09
wi = 100

y = A * np.sin(wi * t + fi)

Y = np.fft.fft(y)
YY = Y * np.conj(Y) / N

plt.plot(t, YY)
plt.savefig('spectral_density.png')
plt.show()


#section 2

teta = np.arange(0, N, 1)
w1 = 81
w2 = 14
b = 5

x = np.sin(w1 * T * teta) + np.cos(w2 * T * teta)

r = b * np.random.rand(N)

y = x + (r - np.mean(r))

plt.plot(teta, x)
plt.title('Полезный сигнал')
plt.savefig('good.png')
plt.show()

plt.plot(teta, r)
plt.title('Шум')
plt.savefig('bad.png')
plt.show()

plt.plot(teta, y)
plt.title('Наложение шума и полезного сигнала')
plt.savefig('ugly.png')
plt.show()

#section 3


r = np.zeros(int(len(y) / 10 - 1))
for i in range(len(r)):
  for j in range(N - i):
      r[i] += y[j] * y[j + i]
  r[i] /= len(y) - i

w = np.linspace(0, np.pi / T, N)
# w = w(1:end-1);
y = np.zeros(len(w))
for n in range(len(w)):
  for m in range(len(r)):
      y[n] += r[m] * np.cos(w[n] * T * m)
  y[n] *= 2


plt.plot(w, y)
plt.title('Спектральная плотность сигнала')
plt.savefig('sig_spectral_density.png')
plt.show()

plt.plot(w, np.abs(y))
plt.title('Спектральная плотность сигнала (абсолюное значение)')
plt.savefig('sig_spectral_density_abs.png')
plt.show()

#section 4

max_num = Search(y)

ww1 = np.pi * max_num[0] / (128 * T)
ww2 = np.pi * max_num[1] / (128 * T)

print(ww1, ww2)

bartletta_window = np.zeros(len(r))
ht = np.arange(0, len(r), 1)
for i in range(len(ht)):
  if ht[i] >= 0 and ht[i] <= len(ht) / 2:
    bartletta_window[i] = 2 * ht[i] / len(ht)
  else:
    bartletta_window[i] = 2 - 2 * ht[i] / len(ht)
    # bartletta_window(i) = 2 - (2*ht(i))/(length(ht));
  # if ht[i] >= 0 and ht[i] <= len(ht):
    # bartletta_window[i] = .42 - .5 * np.cos(2 * np.pi * ht[i] / len(ht)) + .08 * np.cos(4 * np.pi * ht[i] / len(ht))

plt.plot(ht, bartletta_window)
plt.title('Окно Бартлетта')
plt.savefig('bartletta_window.png')
plt.show()

y1 = np.zeros(len(w))
for n in range(len(w)):
  for m in range(len(r)):
    y1[n] += r[m] * bartletta_window[m] * np.cos(w[n] * T * m)
  y1[n] *= 2

plt.plot(w, y1)
plt.title('Спектральная плотность сигнала (Бартлетт)')
plt.savefig('sig_spectral_density_bart.png')
plt.show()

plt.plot(w, np.abs(y1))
plt.title('Спектральная плотность сигнала (Бартлетт) (абсолюное значение)')
plt.savefig('sig_spectral_density_bart_abs.png')
plt.show()

max_num = Search(y1)
ww1_1 = np.pi * max_num[0] / (128 * T)
ww2_2 = np.pi * max_num[1] / (128 * T)

print(ww1_1, ww2_2)