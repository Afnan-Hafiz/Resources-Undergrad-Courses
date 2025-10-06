import numpy as np
def flatten(arr1):
  arr2=np.zeros(arr1.size, dtype=arr1.dtype)
  row=arr1.shape[0]
  column=arr1.shape[1]
  k=0
  for i in range(row):
    for j in range(column):
      arr2[k]=arr1[i][j]
      k+=1
  return arr2

arr1 = np.array( [ [1, 2, 3],[3, 4, 5] ] )
arr2 = flatten(arr1)
print(arr2)