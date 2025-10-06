#home task 3.2
def calc_tax(x,y):
  tax=0
  if x<18 or y<10000:
    tax=0
  elif 10000<=y<=20000:
    tax=(7*y)/100
  elif 20000<y:
    tax=(14*y)/100
  return tax
def calc_yearly_tax():
  x=int(input())
  yearly_tax=0
  for i in range(1, 13):
        y=int(input())
        monthly_tax=calc_tax(x,y)
        yearly_tax+=monthly_tax
        print(f"Month{i} Tax: {int(monthly_tax)}")
  print(f"Total Yearly Tax: {int(yearly_tax)}")
calc_yearly_tax()