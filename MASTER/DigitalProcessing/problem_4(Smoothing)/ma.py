import numpy as np

def MA(X, L):
  N = len(X)
  y = np.zeros(N)

  for n in range(L // 2 - 1, N - L // 2):
    sum_41 = 0
    for k in range(-L // 2, L // 2 + 1):
      print('точка', k)
      print('записываем', n)
      sum_41 += X[n + k]
    y[n] = sum_41 / (L + 1)

  return y

# import numpy as np

# def MA(X, L):
#   N = len(X)
#   y = np.zeros(N)

#   for n in range(N - L - 1):
#     sum_41 = 0
#     for k in range(L + 1):
#       sum_41 += X[n + k]
#     y[n] = sum_41 / (L + 1)

#   return y