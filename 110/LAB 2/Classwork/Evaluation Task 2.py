x=int(input())
a=x//3600
remaining=x%3600
minute=remaining//60
second=remaining %60
print("Hours:",a)
print("Minutes:",minute)
print("Seconds:",second)