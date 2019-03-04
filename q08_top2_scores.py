a = int(input("Number of students: "))
class_list = dict()
count = 0
while count<a:
  data = input('Enter score then name separated by ":": ')
  temp = data.split(':')
  class_list[str(temp[1])] = temp[0]
  count += 1
dictList = []
dictList += class_list.keys()
x = []
for i in dictList:
  x.append(int(i))
x.sort()
largest = x[-1]
print('Number One: {}'.format(class_list[str(largest)]))
second = x[-2]
print('Number Two: {}'.format(class_list[str(second)]))
	
