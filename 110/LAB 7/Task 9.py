import numpy as np
A = np.array([ [1, 5, 12, 1],
                [2, -4, 6, 7],
                [3, 8, 5, 9],
                [3, 5, 23, -6] ])

row=A.shape[0]
column=A.shape[1]
primarySum=0
secondarySum=0
for i in range(row):
  for j in range(column):
    if i==j:
      primarySum+=A[i][j]
    elif j==row-1:
      secondarySum+=A[i][j]
      row-=1

print(abs(primarySum-secondarySum))