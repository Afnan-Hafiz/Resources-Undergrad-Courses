def is_valid_triangle(x,y,z):
  if x+y>z and x+z>y and z+y>x:
    return True
  else:
    return False
result=is_valid_triangle(7,5,10)
print(result)