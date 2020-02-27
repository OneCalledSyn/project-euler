# What is the sum of the digits of the number 2^1000?

import math

def power_digit_sum(n):
  number = 2 ** n
  str_num = str(number)
  total = 0
  for i in str_num:
    total += int(i)
  print(total)  

power_digit_sum(1000)  
