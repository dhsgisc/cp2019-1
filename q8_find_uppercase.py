def find_num_uppercase(a):
  if len(a) == 1:
    if a[0].isupper() == True:
      return 1
    else:
      return 0
  else:
    if a[0].isupper() == True:
      return 1 + find_num_uppercase(a[1:])
    else:
      return find_num_uppercase(a[1:])
