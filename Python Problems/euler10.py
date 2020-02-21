# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# Sieve of Eratosthenes
import math

p = 2000000
potential_primes = []
for x in range (2, p):
  potential_primes.append(x)
  
i = 2
while (i <= int(math.sqrt(p))):
  if i in potential_primes:
    for j in range(i * 2, p, i):
      if j in potential_primes:
        potential_primes.remove(j)
  i += 1
  
print(sum(potential_primes)) 

# Faster Sieve by someone else

def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print (sumPrimes(2000000))
