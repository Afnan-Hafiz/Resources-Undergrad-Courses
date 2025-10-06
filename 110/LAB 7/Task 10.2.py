import numpy as np
arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row=arr1.shape[0]
column=arr1.shape[1]
arr2=np.zeros((column, row), dtype="int")
for i in range(row):
  for j in range(column):
    arr2[j][i]= arr1[i][j]

row1=arr2.shape[0]
column1=arr2.shape[1]
arr3=np.zeros((row1,column), dtype="int")

for i in range(row1):
  for j in range(column):
    sum=0
    for p in range(column1):
      sum+=arr2[i][p]*arr1[p][j]
    arr3[i][j]=sum

print(arr3)