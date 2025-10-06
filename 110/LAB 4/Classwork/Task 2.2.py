a=input()
b=""
new=""
for i in range(len(a)):
  if i%2!=0:
    b+=a[i]
  else:
    continue
for i in b:
  if "a"<=i<="z":
    new+=chr(ord(i)-32)
  else:
    new+=i
print(new)