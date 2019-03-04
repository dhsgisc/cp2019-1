from random import randint
def print_matrix(n):
  for x in range(n):
    counts = 1
    c = []
    d = []
    while counts<=n:
        c.append(str(randint(0,1)))
        counts += 1
    d.append(" ".join(c))
    print(d[0])
count = int(input("Enter Number: "))
print_matrix(count)
