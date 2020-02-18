#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def prime_factors(n):
  prime_factors = []
  while (n % 2 == 0):
    n /= 2
    prime_factors.append(2)
    
  for i in range(3, int(math.floor(n**0.5))+1, 2):
    while (n % i == 0):
      n /= i
      prime_factors.append(i)
  
  print(prime_factors[-1])
  
prime_factors(600851475143)  
