#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

phi = ((1 + math.sqrt(5)) / 2)

def fibonacci_n(digits):
  return math.ceil((math.log10(math.sqrt(5)) + (digits - 1))/ math.log10(phi))

print(fibonacci_n(1000))  
