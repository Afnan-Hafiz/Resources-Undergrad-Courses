def reverse_digits(num):
    if num< 10:
        print(num)
    else:
        print(num%10)
        reverse_digits(num//10)
n=int(input())
reverse_digits(n)