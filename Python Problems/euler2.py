def fibonacci(n):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
  n = 4000000  
  i = 1
  sum = 0
  while fibonacci(i) <= n:
    if (fibonacci(i) % 2 == 0):
      sum += fibonacci(i)
    i += 1
print(sum)
