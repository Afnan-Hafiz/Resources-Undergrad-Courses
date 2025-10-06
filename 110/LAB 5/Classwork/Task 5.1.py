def one_to_N(c,n):
  if c==n:
    print(c, end=" ")
    return
  else:
    print(c, end=" ")
    one_to_N(c+1,n)
n=int(input())
one_to_N(1,n)