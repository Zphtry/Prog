import numpy as np

def R(N):
  b = 1.7
  rl = b * np.random.rand(N)
  k = np.mean(rl)
  y = rl - k
  return y