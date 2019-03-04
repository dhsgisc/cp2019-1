side_1 = int(input("Enter side 1: "))
side_2 = int(input("Enter side 2: "))
side_3 = int(input("Enter side 3: "))
if side_1+side_2 <= side_3:
  print("Invaild Triangle!")
elif side_2+side_3 <= side_1:
  print("Invaild Triangle!")
elif side_1+side_3 <= side_2:
  print("Invaild Triangle!")
else:
  peri = side_1+side_2+side_3
  print("Perimeter is: " + str(peri))

