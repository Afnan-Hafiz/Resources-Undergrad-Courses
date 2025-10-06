str1=""
for i in range(18,64,9):
  if i%2==0:
    str1+=str(i)+", "
  else:
    str1+=str(i*-1)+", "
print(str1[:-2])