# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squared(n):
  total = 0
  for i in range(1, n + 1):
    total += i**2
  return total
  
def squared_sum(n):
  total = 0
  for i in range(1, n + 1):
    total += i
  return (total**2)
  
print(sum_squared(100) - squared_sum(100))  
