import numpy as np

def F(N):
  M1 = 49
  M2 = 23
  y = np.zeros(N)
  for n in range(N):
    y[n] = np.sin((2 * np.pi * (n - 1)) / M1) + np.cos((2 * np.pi * (n - 1)) / M2)

  return y