n = 0 
a = range(12000)
for num in a:
  n = num**2
  if n > 12000:
    print(num)
    break
  else:
    pass
