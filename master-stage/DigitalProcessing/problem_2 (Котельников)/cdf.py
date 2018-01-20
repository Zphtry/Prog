import numpy as np

def CDF(t, T, n):

  if t.any() == n * T:
    return 1

  else:
    return np.sin((np.pi / T) * (t - n * T)) / ((np.pi / T) * (t - n * T))
