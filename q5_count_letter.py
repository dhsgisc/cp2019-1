def count_letter(a, b):
  if len(a) == 1:
    if a == b:
      return 1
    else:
      return 0
  else:
      if a[0] == b:
          return 1 + count_letter(a[1:], b)
      else:
          return count_letter(a[1:], b)
