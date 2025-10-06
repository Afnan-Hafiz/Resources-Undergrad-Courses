def recursive_summation(start,end):
  if end==0 or end==1:
    return 1
  else:
    return end+recursive_summation(start,end-1)
n=int(input())
recursive_summation(1,n)