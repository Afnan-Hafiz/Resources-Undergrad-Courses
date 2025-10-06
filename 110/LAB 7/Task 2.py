import numpy as np
n=int(input("length of array:"))
myarr=np.zeros(n,dtype="int")
for i in range(n):
  myarr[i]=int(input())
print("Original array: ", myarr)
for i in range(n):
  if myarr[i]<0 or myarr[i]==0:
    myarr[i]=0
  else:
    myarr[i]=1
print("After modifying: ", myarr)