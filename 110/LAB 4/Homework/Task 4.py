a=input()
word=""
upperCase=True
for i in a:
  if upperCase:
    word+=i.upper()
  else:
    word+=i.lower()
  upperCase = not upperCase
print(word)