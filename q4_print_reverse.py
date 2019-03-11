def reverse_int(n):
  if len(str(n)) == 1:
    return n
  else:
    a = str(n)
    return a[-1]+reverse_int(a[:-1])
