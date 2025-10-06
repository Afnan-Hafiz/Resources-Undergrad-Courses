def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return False
      break
  else:
    return True
prime_check = is_prime(20)
print(prime_check)