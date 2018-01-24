import numpy as np

def EM(X, a):
  N = len(X)
  y = np.zeros(N)
  for n in range(N):
    for v in range(n):
      y[n] += + a * (X[n - v] * ((1 - a) ** v) + X[0]*((1 - a) ** n))

  return y