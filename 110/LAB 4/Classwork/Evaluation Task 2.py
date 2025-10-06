a=input()
vow=0
cons=0
for i in a:
  if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i=="I" or i=="U":
    vow+=1
  else:
      cons+=1
if vow%3==0 and cons%5==0:
  print("Aaarr! Me Plunder!!")

else:
  print("Blimey! No Plunder!!")