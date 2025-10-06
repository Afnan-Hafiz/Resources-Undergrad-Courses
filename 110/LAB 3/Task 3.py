num=int(input())
while 0<num:
  new=num%10
  remainNum=num//10
  num=remainNum
  if num==0:
    print(new)
  else:
    print(new,end=",")
