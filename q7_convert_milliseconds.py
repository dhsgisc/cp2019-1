def convert_ms(n):
  sec = n//1000
  hour = 0
  min = 0
  if sec >= 60:
    min = sec//60
    sec -= (min*60)
  if min >= 60:
    hour = min//60
    min -= (hour*60)
  print("{}:{}:{}".format(hour,min,sec))
