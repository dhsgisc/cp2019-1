def sum_series1(i):
  if i == 1:
    return 1
  else:
    n = 1/i
    return n + sum_series1(i-1)
