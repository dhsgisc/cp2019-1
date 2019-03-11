def sum_digits(n):
  n = str(n)
  if len(n) == 1:
    return int(n)
  else:
    return int(n[0])+int(sum_digits(n[1:]))
