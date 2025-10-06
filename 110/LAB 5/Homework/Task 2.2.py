def show_palindrome(n):
  for i in range(1,n+1,1):
    print(i,end="")
  for i in range(n-1,0,-1):
    print(i,end="")
show_palindrome(5)