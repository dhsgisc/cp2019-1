def m_series(i):
  count=0
  s=0
  while count<=i:
    s+=i/(i+1)
    count+=1
  print("{}     {}".format(i,round(s,4)))
counts=1
print("i"+"     "+"m(i)")
while counts<=20:
  m_series(counts)
  counts+=1
