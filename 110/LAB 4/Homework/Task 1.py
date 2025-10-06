a=input()
p=""
for i in a:
  if p=="" or i!=p[len(p)-1]:
    p=p+i
  else:
    continue
print(p)