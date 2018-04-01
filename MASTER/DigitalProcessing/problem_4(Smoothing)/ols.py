def OLS(Y,F):
  y = 0
  for n in range(len(Y) - 20):
    y += (abs(Y[n + 10] - F[n + 10])) ** 2

  return y