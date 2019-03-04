miles = 1
a = []
while miles<=10:
  kilometers=miles*1.609
  a.append(tuple((miles, round(kilometers, 3))))
  miles+=1
b = []
x = range(20, 70, 5)
for i in x:
  m=i/1.609
  b.append(tuple((i, round(m, 3))))
c = []
no = 0
while no <= 9:
  c.append(a[no])
  c.append(b[no])
  no += 1
d = []
g = 0
h = 1
while h<= 20:
  d.append(tuple((c[g] + c[h])))
  g += 2
  h += 2
print("Miles Kilometers Miles Kilometers")
for i, j, k, l in d:
  print('{}     {}      {}    {}'.format(i, j, k, l))
