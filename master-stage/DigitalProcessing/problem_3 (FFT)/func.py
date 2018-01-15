import numpy as np

def Func(t):
  A   = [    1,      2,    10]
  f   = [10000,  20000, 40000]
  Phi = [.5236, 2.0944, .7854]

  y = 0
  for k in range(3):
    y += A[k] * np.sin(t * np.pi * f[k] + Phi[k])
  return y