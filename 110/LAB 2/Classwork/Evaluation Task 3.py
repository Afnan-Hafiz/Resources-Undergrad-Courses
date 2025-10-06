x=int(input())
y=int(input())
z=float(x/y)
p=(z*(3600/1000))
if z<60:
  print(int(z))
  print("Too slow. It need more changes.")
elif 60<=z and z<=90:
  print(int(z))
  print("velocity is ok. The car is ready!")
elif 90<z:
  print(int(z))
  print("Too fast. Only a few changes should suffice.")