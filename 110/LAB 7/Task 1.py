import numpy as np
n=int(input("length of array:"))
myarr=np.zeros(n,dtype="int")
for i in range(n):
  myarr[i]=int(input())
print("Original Array:" ,myarr)
new=myarr.size+1
myarr2=np.zeros(new,dtype="int")
p=int(input())
for i in range(n):
  myarr2[i]=myarr[i]
  myarr2[-1]=p
print("Resized Array:", myarr2)