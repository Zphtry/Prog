import numpy as np

def MA(X, L):
  N = len(X)
  y = np.zeros(N)

  # for n =L/2+1:N-L/2
  # for n = L / 2 + 1 : N - L / 2
  for n in range(L // 2 + 1, N - L // 2):
    sum_41 = 0
    # for k = -L/2:L/2
    for k in range(-L // 2, L // 2):
      sum_41 += X[n + k]
    y[n] = sum_41 /(L + 1)

  return y