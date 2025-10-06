def show_dots(num):
    print("." * num, end="")
def show_palindrome(n):
  for i in range(1,n+1,1):
    print(i,end="")
  for i in range(n-1,0,-1):
    print(i,end="")
def show_triangle(num):
    length=(num*2)-1
    for i in range(1,num+1):
        numeric=(i*2)-1
        dot= int((length-numeric)/2)
        show_dots(dot)
        show_palindrome(i)
        show_dots(dot)
        print()
show_triangle(5)