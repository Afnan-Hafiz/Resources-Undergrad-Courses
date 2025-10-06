hour=int(input())
if hour>0 and hour<=168:
  if hour<=40:
    print(hour*200)
  elif (hour>40):
   print(8000+(hour-40)*300)
elif hour<0:
    print("hour cannot be negative")
else:
    print("impossible to work more than 168 hours weekly")