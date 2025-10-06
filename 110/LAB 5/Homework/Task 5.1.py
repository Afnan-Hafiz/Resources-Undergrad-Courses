def sequence_recursive(N) :
  a=0
  if N==1:
    return N
  if N%2==0 :
    a=(-1)*N
  else :
    a=N
  return a+sequence_recursive(N-1)
n=int(input())
print(sequence_recursive(n))