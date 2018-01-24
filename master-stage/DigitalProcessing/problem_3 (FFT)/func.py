import numpy as np

def Func(t):
  A   = [    .5,    1,    5]
  f   = [1000,  3000, 6000]
  Phi = [np.pi / 3, np.pi, np.pi / 2]

  y = 0
  for k in range(3):
    y += A[k] * np.sin(t * np.pi * f[k] + Phi[k])
  return y