def sequence_iterative(N):
    result=0
    for i in range(1,N+1):
        if i%2==0:
            result-=i
        else:
            result+=i
    return result
n=int(input())
print(sequence_iterative(n))