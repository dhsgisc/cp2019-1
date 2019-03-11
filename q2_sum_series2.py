def sum_series2(i):
  if i == 1:
    return 1/3
  else:
    n = i/((2*i)+1)
    return n + sum_series2(i-1)
