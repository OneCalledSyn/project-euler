# What is the value of the first triangle number to have over five hundred divisors?


#First try (failure)
import math

n = 5
divisors = 1
number = 6
x = 4

while True:
  for i in range(2, math.floor(number/2) + 2):
    if number % i == 0:
      divisors += 1
  if divisors = n:
      break
  number += x
  x += 1
  divisors = 1
  
print(number)


# Second try: What did I learn?
# Tau(n), which gives the number of divisors, is the product of the degree of each prime factor + 1
# How to get program runtime using timeit module

import timeit

start = timeit.default_timer()

def tau(number):
  n = number
  p = 2
  e = 1
  
  if number == 1:
    return 1
  
  while (p * p <= n):
    counter = 1
    while (n % p == 0):
      n /= p
      counter += 1
    p += 1
    e *= counter
  
  if (n == number or n > 1):
    e *= 1 + 1
  return e
  
def euler12(n):
  x = 1
  y = 1
  
  while tau(y) < n :
    x += 1
    y += x
  return y
  
print(euler12(501))  
  
stop = timeit.default_timer()

print('Program Runtime: ', stop - start) 
