import numpy as np
n=int(input())
arr1=np.zeros(n,dtype="int")
for i in range(n):
  p=int(input())
  arr1[i]=p
print("Original Array:", arr1)

for i in range(0,n-1):
  minInd=arr1[i]
  swap=arr1[i]
  curr=i
  for j in range(i+1,n):
    if arr1[j]<minInd:
      minInd=arr1[j]
      curr=j
  arr1[i]=minInd
  arr1[curr]=swap
print("Sorted Array:",arr1)