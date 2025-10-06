def is_perfect(num):
  count=0
  for i in range(1,num):
    if num%i==0:
      count+=i
  if count==num:
    return True
  else:
    return False
perfect_check = is_perfect(6)
print(perfect_check)