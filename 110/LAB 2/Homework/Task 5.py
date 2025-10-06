marks=int(input())
if 0<=marks<=100:
  if 90<=marks<=100:
   print("A")
  if 80<=marks<=89:
   print("B")
  if 70<=marks<=79:
   print("C")
  if 60<=marks<=69:
   print("D")
  if 50<=marks<=59:
   print("E")
  if marks<50:
   print("F")
else:
  print("No output")
