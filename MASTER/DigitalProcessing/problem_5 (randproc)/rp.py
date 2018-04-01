import numpy as np

def RP(N, a, b):
  y = np.zeros(N)
  x = b * np.random.rand(N)
  y[0] = b / 2

  for n in range(1, N):
    y[n] = y[n - 1] * (1 - a) + a * x[n]

  return y