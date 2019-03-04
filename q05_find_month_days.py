year = int(input("Enter year: "))
month = int(input("Enter month: "))
days_30 = [4, 6, 9, 11]
if month == 2:
  if (year%4==0 and year%100!=0) or year%400==0:
    print("29 days")
  else:
    print("28 days")
else:
  if month in days_30:
    print("30 days")
  else:
    print("31 days")
