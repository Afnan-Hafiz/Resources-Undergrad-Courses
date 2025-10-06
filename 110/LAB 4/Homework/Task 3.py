a=input()
word=""
for i in a:
  if 97 <= ord(i) <=122:
    if ord(i)==122:
      word+="a"
    else:
      word+=chr(ord(i)+1)
  elif ord(i)==32:
    word+="!"
  else:
    print("Please use small letters")
print(word)