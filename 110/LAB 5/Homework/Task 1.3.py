def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return False
      break
  else:
    return True
def is_perfect(num):
  count=0
  for i in range(1,num):
    if num%i==0:
      count+=i
  if count==num:
    return True
  else:
    return False
def special_sum(n):
  sum=0
  for i in range(0,n+1):
    if(is_prime(i)):
      sum+=i
    elif(is_perfect(i)):
      sum+=i
  return sum-1
n=int(input())
result= special_sum(n)
print(result)