import numpy as np
import matplotlib.pyplot as plt

# from search import Search

#section 1

N = 2 ** 11

teta = np.arange(0, N, 1)
T = .02
w1 = 81
w2 = 14
b = 5

f = np.sin(w1 * T * teta) + np.cos(w2 * T * teta)

r1 = b * np.random.rand(N)
r = r1 - np.mean(r1)

x = f + r;

plt.plot(teta, f)
plt.title('Чистая последовательность')
plt.savefig('good.png')
plt.show()

plt.plot(teta, r)
plt.title('Шум')
plt.savefig('bad.png')
plt.show()

plt.plot(teta, x)
plt.title('Наложение шума на чистую последовательность')
plt.savefig('ugly.png')
plt.show()


#section 2

D = .5
L = int(N / 2)
V = int((N - D * L) / (L - D * L))
print(V)

teta1 = np.arange(0, L, 1)
x1 = np.zeros((V, L))

for i in range(L):
  x1[0, i] = x[i]
  x1[1, i] = x[i + 64]
  x1[2, i] = x[i + 128]

plt.plot(teta1, x1[0, :])
plt.title('Первый сегмент')
plt.savefig('first_seg.png')
plt.show()

plt.plot(teta1, x1[1, :])
plt.title('Второй сегмент')
plt.savefig('second_seg.png')
plt.show()

plt.plot(teta1, x1[2, :])
plt.title('Третий сегмент')
plt.savefig('third_seg.png')
plt.show()

#section 3

w = np.zeros(L)
for i in range(L):
    if 0 <= teta[i] <= (L - 1) / 2:
        w[i] = 2 * teta[i] / (L - 1)

    else:
        w[i] = 2 - (2 * teta[i]) / (L - 1)

plt.plot(teta1, w)
plt.title('Окно Бартлетта')
plt.savefig('bart_window.png')
plt.show()


y = np.zeros((V, L))
for i in range(V):
  for j in range(L):
    y[i, j] = x1[i, j] * w[j]

S = np.zeros((V, L))

for i in range(V):
  S[i, :] = np.fft.fft(y[i, :])

plt.plot(teta1, S[0,:])
plt.title('Спектральная характеристика (сег 1)')
plt.savefig('spec_1.png')
plt.show()

plt.plot(teta1, S[1,:])
plt.title('Спектральная характеристика (сег 2)')
plt.savefig('spec_2.png')
plt.show()

plt.plot(teta1, S[2,:])
plt.title('Спектральная характеристика (сег 3)')
plt.savefig('spec_3.png')
plt.show()

P = np.zeros((V, L))
for i in range(V):
  for j in range(L):
    P[i, j] = (1 / N) * S[i, j] ** 2;

plt.plot(teta1, P[0,:])
plt.title('Периодограмма (сег 1)')
plt.savefig('period_1.png')
plt.show()

plt.plot(teta1, P[1,:])
plt.title('Периодограмма (сег 2)')
plt.savefig('period_2.png')
plt.show()

plt.plot(teta1, P[2,:])
plt.title('Периодограмма (сег 3)')
plt.savefig('period_3.png')
plt.show()

# section 4

ww1 = Search(S[0, :], T, 200)
ww2 = Search(S[1, :], T, 95)
ww3 = Search(S[2, :], T, 200)

print(ww1)
print(ww2)
print(ww3)
