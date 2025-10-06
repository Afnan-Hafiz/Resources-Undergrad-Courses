y=float(input())
x=int(input())
if x>=30 and 3.80<=y<=3.89:
  print("The student is eligible for a waiver of 25 percent")
elif x>=30 and 3.90<=y<=3.94:
  print("The student is eligible for a waiver of 50 percent")
elif x>=30 and 3.95<=y<=3.99:
  print("The student is eligible for a waiver of 75 percent")
elif x>=30 and y==4.00:
  print("The student is eligible for a waiver of 100 percent")
else:
  print("The student is not eligible")