kilograms = 1
a = {}
while len(a.keys())<10:
  pounds=kilograms*2.2
  a[kilograms]=round(pounds,1)
  kilograms+=1
print("Kilograms Pounds")
for b, c in a.items():
  print('{} {}'.format(b, c))

# 1 pound = 2.2 kg
for i in range(1,11):
  print("{0:<10}{1:.1f}".format(i, i*2.2))
