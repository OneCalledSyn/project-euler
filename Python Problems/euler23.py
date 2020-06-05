# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Plan: Check 12 through 28123 iteratively to see if it is abundant. Add all abundant numbers into an array.
# Add every array element to every other element to generate a list of abundant sums
# Calculate the total abundant sum and subtract it from the sum of all numbers between 1 and 28123

# Extra knowledge: Every number greater than 20161 is an abundant sum
#                  Prime numbers aren't abundant
#                  All even numbers greater than 46 are an abundant sum
#                  All multiples of a perfect number are abundant
#                  All positive multiples of abundant numbers are also abundant
#                  Any positive multiple (greater than 1) of a perfect number is an abundant number

import math

abundant_nums = []

for i in range(12, 20161):
  divisor_sum = 1
  for j in range(2, math.ceil(math.sqrt(i))):
    if (i % j == 0):
      divisor_sum += j + i/j
  if divisor_sum > i:
    abundant_nums.append(i)

    
print(abundant_nums)  


abundant_sums = []

for i in abundant_nums:
  for j in abundant_nums:
    if (i + j <= 28123):
      abundant_sums.append(i + j)
      
print(abundant_sums)      
