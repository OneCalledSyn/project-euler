# Find the sum of the digits in the number 100!

import math

def factorial_digit_summer(n):

  return(sum(map(int, str(math.factorial(n)))))

print(factorial_digit_summer(100))

# Takeaway:
# Stirling's Approximation for estimating factorials
