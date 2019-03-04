a = input("Enter name: ")
b = float(input("Enter number of hours worked weekly: "))
c = float(input("Enter hourly pay rate: "))
d = float(input("Enter CPF contribution rate(%): "))
x = b*c
y = x*(d/100)
z = x - y
print("Payroll statement for {}\nNumber of hours worked in week: {}\nHourly pay rate: ${}\nGross pay = ${}\nCPF contribution at 20% = ${}\nNet pay = ${}".format(a, b, c, x, y, z))
