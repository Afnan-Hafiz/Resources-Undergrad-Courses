def calc_tax(x,y):
  tax=0
  if x<18 or y<10000:
    tax=0
  elif 10000<=y<=20000:
    tax=(7*y)/100
  elif 20000<y:
    tax=(14*y)/100
  return tax
t = calc_tax(20,18000)
print(int(t))