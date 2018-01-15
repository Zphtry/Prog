import numpy as np

def CDF(t, T, n):

  if t == n * T:
    return 1

  else:
    return np.sin((np.pi / T) * (t - n * T)) / ((np.pi / T) * (t - n * T))


# function y = CDF(t,T,n)
#   if t == n*T
#       y = 1;
#       return;
#   else 
#       y = sin((pi/T)*(t-n*T))/((pi/T)*(t-n*T));
#       return;
#   end
# end