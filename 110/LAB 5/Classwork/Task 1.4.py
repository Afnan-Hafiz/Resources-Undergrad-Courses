def is_pos(num):
  if num>0:
    return True
  else:
    return False
def is_even(num):
  if num%2==0:
    return True
  else:
    return False
def sequence(n):
  if is_pos(n)==True:
    for i in range(0,n+1):
      if is_even(i)==True:
        print(i,end=" ")
  else:
    for i in range(n,0):
      if is_even(i)==False:
        print(i,end=" ")
sequence(10)
