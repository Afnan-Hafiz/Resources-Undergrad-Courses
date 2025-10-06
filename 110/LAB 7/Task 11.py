arr1 = np.array([[4,1,2],
                  [9,3,7]])

row=arr1.shape[0]
column=arr1.shape[1]
difference=abs(row-column)
remainder=difference%row
sum=0
for i in range(row):
  if i==remainder:
    for j in range(column):
      sum+= arr1[i][j]
    average=sum/column
average=round(average,2)

finalArr=np.zeros((row,column), dtype="float")
for i in range(row):
  for j in range(column):
    finalArr[i][j]=arr1[i][j]*average

print(finalArr)