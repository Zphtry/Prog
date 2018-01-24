import numpy as np

def R(N):
  b = 2
  rl = b * np.random.rand(N)
  k = np.mean(rl)
  y = rl - k
  return y