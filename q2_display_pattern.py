def display_pattern(num):
  count = 1
  a =[]
  while count<=num:
    a.append(str(count))
    b = a[::-1]
    c = " ".join(b)
    print("{:>15}".format(c))
    count += 1
