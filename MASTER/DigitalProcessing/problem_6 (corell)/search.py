import numpy as np

# function max_num = poisk(y)
# max_number = max(y);
# current = 0;
# for i = 1:length(y)
#     if (y(i) ~= max_number) && (y(i) > current) 
#         current = y(i);
#     end
# end
# max_num = [max_number current];
# return;
# end


def Search(y):
  max_number = np.max(y)
  current = 0
  for i in range(len(y)):
    if y[i] != max_number and y[i] > current:
      current = y[i]
  return np.array([max_number, current])