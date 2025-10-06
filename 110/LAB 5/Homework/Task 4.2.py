def power(a, n):
    if n==0:
      return 1
    else:
      return a*power(a,n-1)
a=int(input())
n=int(input())
print(power(a,n))