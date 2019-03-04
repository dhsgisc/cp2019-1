n1 = int(input("Enter First Number: "))
n2 = int(input("Enter First Number: "))
a = []
for num in range(1,n1):
  if n1%num==0 and n2%num==0:
    a.append(num)
a.sort()
print(a[-1])
