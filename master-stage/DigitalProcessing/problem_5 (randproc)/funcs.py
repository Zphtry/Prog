import numpy as np


def R(X, M):
  N = len(X)
  L = N // 10 - 1
  y2 = np.zeros(L)

  for m in range(L):
    for n in range(N - m):
      y2[m] += (X[n] - M) * (X[n + m] - M)
    y2[m] /= N - m

  y = np.append(np.flip(y2, axis=0), y2)
  return y