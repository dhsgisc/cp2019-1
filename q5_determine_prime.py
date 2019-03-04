def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
factors = []
count = 2
while len(factors) <= 1000:
  if is_prime(count) == True:
    factors.append(str(count))
  count+=1
a = []
b = 0
c = 10
while c<=999:
  a.append(tuple(factors[b:c]))
  b+=10
  c+=10
d =[]
for i in a:
  d.append(" ".join(i))
for p in d:
  print(p)
