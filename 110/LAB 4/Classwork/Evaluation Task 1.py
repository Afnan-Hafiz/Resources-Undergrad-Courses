a=input()
count=0
for i in a:
  if i=="0" or i=="1":
    continue
  else:
    count+=1
    break
if count==0:
  print("Binary")
else:
  print("Not Binary")