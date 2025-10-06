import numpy as np
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
sum=0
len=vec1.size
for i in range(len):
    sum+= vec1[i]*vec2[i]
print("Dot product:",sum)
if sum%2==0:
 for i in range(0,len,2):
  temp=vec1[i]
  vec1[i]=vec2[i]
  vec2[i]=temp
else:
  for i in range(1,len,2):
    temp=vec1[i]
    vec1[i]=vec2[i]
    vec2[i]=temp
print("After Swapping:")
print(vec1)
print(vec2)