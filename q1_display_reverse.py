def reverse_int(num):
  digits = []
  reverse = []
  for digit in str(num):
    digits.append(digit)
    reverse = reversed(digits)
  a = int("".join(reverse))
  print(a)
