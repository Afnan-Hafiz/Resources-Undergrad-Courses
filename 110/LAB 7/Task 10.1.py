import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

row=A.shape[0]
column=A.shape[1]
arr1=np.zeros((column,row), dtype="int")
for i in range(row):
  for j in range(column):
    arr1[j][i]= A[i][j]
print(arr1)