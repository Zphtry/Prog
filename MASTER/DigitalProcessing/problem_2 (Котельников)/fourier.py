import numpy as np

def _fourier(func, t, om):
  fou = []
  for i in range(min(len(t), len(om))):
    '''метод трапеций'''
    re = np.trapz(np.multiply(func, np.cos(t * om[i])), x=t)
    im = np.trapz(np.multiply(func, np.sin(t * om[i])), x=t)
    fou.append(re - im * 1j)
  return np.array(fou)