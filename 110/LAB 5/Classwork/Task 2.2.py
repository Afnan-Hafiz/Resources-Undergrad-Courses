def is_valid_triangle(x,y,z):
  if x+y>z and x+z>y and z+y>x:
    return True
  else:
    return False
def tri_area(x,y,z):
  s = (x + y + z)/2
  area=((s*(s-x)*(s-y)*(s-z))**(1/2))
  if is_valid_triangle(x,y,z)==True:
    print(area)
  else:
    print("Cant form triangle")
tri_area(7,5,10)