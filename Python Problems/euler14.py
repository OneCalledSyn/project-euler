# Which Collatz Conjecture starting number under one million produces the longest chain?

import math

n = 1000000
max_len = 0

for i in range(math.floor(n/2) + 1, n, 2):
  length = 0
  value = i
  print(str(i) + 'i')
  while value > 1:
    if value % 2 == 0:
      value /= 2
      print(str(value) + 'value')
      length += 1
      print(str(length)+ 'length')
    else:
      value = (3*value + 1)
      length += 1
  if length > max_len:
    max_len = length
  length = 0

print(max_len)
