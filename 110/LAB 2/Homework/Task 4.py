time=int(input())
if time<=24:
  if 0<=time<=3 or 7<=time<=11 or 14<=time<=15 or 18==time or 21<=time<=23:
    print("patience is virtue")
  if 4<=time<=6:
    print("breakfast")
  if 12==time==13:
    print("lunch")
  if 16==time==17:
    print("snacks")
  if 19==time==20:
    print("dinner")
  if time<0 or time==24:
    print("wrong time")
else:
  print("wrong time")
