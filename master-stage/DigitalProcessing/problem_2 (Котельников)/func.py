import numpy as np

A, tau = 2, .5
def _func(t):

  return A * np.exp(-t / tau) if 0 <= t.all() < ([t[-1]] * len(t)).all()  else 0

# function y = Func(t,T)
#   if t>=0 && t<=T
#       y = 2*exp(-t/0.5);
#       return;
#   end
#       y = 0;
#       return;
# end