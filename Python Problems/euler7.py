# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# generate natural numbers in order
# check if a number is prime
# if prime, increment counter
# once counter reaches 10001, print value


#First failed attempt
import math

candidate = 4
counter = 2

while counter < 10:
  for i in range(2, math.floor(candidate)):
    if candidate % i == 0:
      print(str(candidate) + " composite")
      candidate += 1
    else:
      print(str(candidate) + " prime")
      counter += 1
      candidate += 1

print(candidate) 

#Second failed attempt
candidate = 3
count = 1
    
    while count != 10001:
        primality = True
        
        for i in range(2, int(math.sqrt(candidate) + 1)):
            if candidate % i == 0: 
                primality = False
                candidate += 2
                break
        
        if primality:
            count += 1
        
        candidate += 2
   
    print(candidate)
    
# Points of interest:
# 1. All primes greater than 3 are in the form 6k-1 or 6k+1
# 2. There are upper and lower bounds on the nth prime
# 3. Sieve of Eratosthenes can be used to generate prime numbers up to a certain number
# 4. Combining the upper bound and the Sieve produces 

# Third attempt

from math import log, ceil
import math

def upper_bound_nth_prime(n):
  if n < 6:
    return 13
  return ceil(n * (log(n) + log(log(n))))

p = 10001

potential_primes = []
for x in range (2, upper_bound_nth_prime(p) + 1):
  potential_primes.append(x)
  
i = 2
while (i <= int(math.sqrt(upper_bound_nth_prime(p)))):
  if i in potential_primes:
    for j in range(i * 2, upper_bound_nth_prime(p) + 1, i):
      if j in potential_primes:
        potential_primes.remove(j)
  i += 1
  
print(potential_primes[10000])  
