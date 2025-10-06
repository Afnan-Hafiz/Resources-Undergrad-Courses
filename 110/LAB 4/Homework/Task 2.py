a=input()
index=0
for i in range(len(a)):
  if a[i]==",":
    index=i
s1=a[:index]
s2=a[index+2:]
z=""
i=0
while i<len(s1) and i<len(s2):
  z+=s1[i]+s2[i]
  i+=1
z+=s1[i:]+s2[i:]
print(z)