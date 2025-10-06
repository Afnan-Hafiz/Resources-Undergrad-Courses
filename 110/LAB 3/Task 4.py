num=int(input())
divisor=0
count=1
while count<=num:
  if num%count==0:
    print(count)
    count+=1
    divisor+=1
  else:
    count+=1
print("Total",divisor,"divisors")