n = 0 
a = range(12000)
x = []
for num in a:
  n = num**3
  if n < 12000:
    x.append(num)
  else:
    pass
x.sort()
print(x[-1])
