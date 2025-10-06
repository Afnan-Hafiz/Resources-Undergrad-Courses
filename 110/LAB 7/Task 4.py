import numpy as np
def printPairs(arr,n):
  count=0
  for i in range(arr.size):
    for j in range(i+1, arr.size):
      if arr[i]+arr[j]==n:
        count+=1
        print(arr[i], arr[j])
  if count==0:
    print("No pair found")

arr1 = np.array([7,8,10,5,3,4,2])
printPairs(arr1, 15)