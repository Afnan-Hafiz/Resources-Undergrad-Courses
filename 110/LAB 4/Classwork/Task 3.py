str1=input()
split=input()
final=""
for i in str1:
  if i==split:
    print(final)
    final=""
  else:
    final+=i
print(final)