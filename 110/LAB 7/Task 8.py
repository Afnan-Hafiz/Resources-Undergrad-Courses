import numpy as np
arr1 = np.array([ [1, 0, 0, 1],
                  [0, 1, 0, 0],
                  [1, 0, 1, 0],
                  [0, 1, 0, 1] ])

row=arr1.shape[0]
column=arr1.shape[1]
identity=True
for i in range(row):
  for j in range(column):
    if i == j and arr1[i][j] != 1:
        identity=False
        break
    elif i!=j and arr1[i][j] != 0:
        identity=False
        break
  if not identity:
    break

if identity==True:
  print("Identity Matrix")
else:
  print("Not an Identity Matrix")