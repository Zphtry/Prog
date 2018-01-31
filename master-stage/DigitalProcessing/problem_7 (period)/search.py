def Search(S, T, number):
  ix = S > number
  mask(2:length(ix) + 1) = ix
  nd = find(mask)

  k1 = np.ceil(abs(S(nd[0])))
  k2 = np.ceil(abs(S(nd[1])))

  w1 = np.pi * k1/(512 * T)
  w2 = np.pi * k2/(512 * T)
  ww = [w1 w2]
  return ww