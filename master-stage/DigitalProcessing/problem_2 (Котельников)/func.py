import numpy as np

A, tau = 2, .5
def _func(t, t_max):

  # return A * np.exp(-t / tau)
  return A * np.exp(-t / tau) if 0 <= t < t_max  else 0

# function y = Func(t,T)
#   if t>=0 && t<=T
#       y = 2*exp(-t/0.5);
#       return;
#   end
#       y = 0;
#       return;
# end