import numpy as np

def dft_exp(k, n, N):
  return np.exp((-1j * 2 * np.pi * n * k) / N)