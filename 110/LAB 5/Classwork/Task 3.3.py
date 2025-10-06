def circle(n):
  area=3.1416*(n**2)
  return area
def sphere(n):
  volume=4/3*3.1416*(n**3)
  return volume
def fitting(a,b,c):
  if c==2:
    area1=circle(a/2)
    area2=circle(b/2)
    if area1>area2:
      remaining_space1=area1-area2
      print(f"Circle-1 can fit inside Circle-2 and {remaining_space1} square units would be left.")
    elif area2>area1:
      remaining_space2=area2-area1
      print(f"Circle-1 can fit inside Circle-2 and {remaining_space2} square units would be left.")
    else:
      print("Impossible to fit.")
  elif c==3:
    volume1=sphere(a/2)
    volume2=sphere(b/2)
    if volume1>volume2:
      remaining1=volume1-volume2
      print(f"Sphere-2 can fit inside Sphere-1 and {remaining1} cubic units would be left.")
    elif volume1<volume2:
      remaining2=volume2-volume1
      print(f"Sphere-1 can fit inside Sphere-2 and {remaining2} cubic units would be left.")
    else:
      print("Impossible to fit.")
fitting(8,10,2)