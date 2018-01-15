import numpy as np
from w import W

def DFT(X):
  N = len(X)
  V = np.log2(N)


  if V % 2 != 0:
    V = np.ceil(V)
    AddN = 2 ** V - N
    X = np.concatenate([X, np.zeros(int(AddN))])
    N = len(X)

  y = []

  if N == 2:
    y.append(X[0] + X[1])
    y.append(X[0] - X[1])
    return y
  
  else:
    E  = np.zeros(N // 2)
    O  = np.zeros(N // 2)

    Ek = 0
    Ok = 0

    for k in range(N):

      if k % 2 == 0:
        E[Ek] = X[k]
        Ek += 1

      else:
        O[Ok] = X[k]
        Ok += 1

    X1 = DFT(E)
    X2 = DFT(O)

    for k in range(N):
      if k < N / 2:
        y.append(X1[k] + W(k - 1, 1, N) * X2[k])
      
      else:
        y.append(X1[k - N // 2] - W(k - N // 2 - 1, 1, N) * X2[k - N // 2])

    return y


print(DFT([3, 4, 5, 0]))
