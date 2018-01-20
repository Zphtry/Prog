A, tau = 2, .5
def _func(arg):

  return A * np.exp(-arg / tau) if 0 <= arg.all() < t[-1] else 0