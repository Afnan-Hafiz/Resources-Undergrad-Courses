s=int(input(""))
a=(3000-125*(s**2))
b=(12000/(4+((s**2)/14900)))
if s<100:
  print(a)
elif 100<=s:
  print(b)