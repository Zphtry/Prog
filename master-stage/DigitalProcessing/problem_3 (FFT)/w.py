import numpy as np

def W(k, n, N):
  return np.exp((-1j * 2 * np.pi * n * k) / N)