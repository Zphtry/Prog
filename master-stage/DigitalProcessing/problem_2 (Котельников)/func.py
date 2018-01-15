import numpy as np

def Func(t, T):
  if 0 <= t <= T:
      return 2 * np.exp(-t / .5)
  return 0

# function y = Func(t,T)
#   if t>=0 && t<=T
#       y = 2*exp(-t/0.5);
#       return;
#   end
#       y = 0;
#       return;
# end