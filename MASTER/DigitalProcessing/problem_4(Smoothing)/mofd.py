import numpy as np

def MoFD(X):
  N = len(X)
  y = np.zeros(N)
  for n in range(2, N - 2):
    y[n] = (-3 * X[n - 2] + 12 * X[n - 1] + 17 * X[n] + 12 * X[n + 1] - 3 * X[n + 2]) / 35

  return y