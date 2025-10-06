def reverse_printing(start,end):
  if end==start:
    print(end, end=" ")
  else:
    print(end, end=" ")
    reverse_printing(start,end-1)
n=int(input())
reverse_printing(1,n)